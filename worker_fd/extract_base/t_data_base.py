import hashlib
import platform
from abc import abstractmethod
import os
import importlib
import time

from sqlalchemy import create_engine
from TopSpeedData_Worker.connection import connect_mysql
from TopSpeedData_Worker.connection.connect import Connect
from TopSpeedData_Worker.connection.oracle import connect_target, connect_source
from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase
from settings import logger
from validation.validation import TValidationObject

CONST_SEPARATOR = '$*'

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置字符集，防止中文乱码


class TDataBaseConfig(object):
    def __init__(self, taskid):
        #源表数据库连接
        self.read_server_user = None
        self.read_server_pass = None
        self.read_server_address = None
        self.read_service_name = None
        # 加载数据库中其他字段
        self.target_orm_name = None
        self.source_orm_name = None
        self.target_table_name = None
        self.source_table_name = None
        self.update_date = None
        self.sql = None
        self.sql1 = None
        self.vc_orm = None
        self.vc_source = None
        self.conn_mysql = connect_mysql()
        self.load_config(taskid)
        # 连接数据库
        sysstr = platform.system()
        if sysstr == "Linux":
            self.conn_source = self.connect_source()
        else:
            self.conn_source = connect_source()
        self.conn_target = connect_target()

    def load_config(self, taskid):
        self.conn_mysql.execute_ext(
            "update t_status set l_status = 1 where l_taskid = {} ".format(taskid))  # 更改表格状态为运行中
        self.conn_mysql.save()
        data = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(taskid))[
            0]  # 读取mysql所有配置
        module_source = importlib.import_module('model.' + "{}".format(data[3]))  # 源表模块
        module_target = importlib.import_module('model.' + "{}".format(data[4]))  # 目标表模块
        self.source_orm_name = getattr(module_source, '{}'.format(data[1]))  # 源表类名
        self.target_orm_name = getattr(module_target, '{}'.format(data[2]))  # 目标表类名
        self.update_date = data[5]  # 更新日期
        self.target_table_name = data[4]  # 目标表名
        self.source_table_name = data[3]  # 源表表名
        self.sql = data[6]  # 目标表sql语句
        self.sql1 = data[7]  # 目标表sql删除语句
        self.vc_orm = data[8]  # 源表orm语句
        self.vc_source = data[9]  # 数据来源

        db_data = self.conn_mysql.execute('select * from t_db_connection_info where id = {}'.format(self.vc_source))[
            0]  # 读取mysql所有配置
        self.read_server_user = db_data[3]
        self.read_server_pass = db_data[11]
        self.read_server_address = db_data[7]
        self.read_service_name = db_data[1]

    def connect_source(self):
        engine_target = create_engine("oracle+cx_oracle://{}:{}@{}/{}".format(
            self.read_server_user,
            self.read_server_pass,
            self.read_server_address,
            self.read_service_name), coerce_to_unicode=True, max_overflow=100, pool_size=100, pool_recycle=3600)
        return Connect(engine_target)

class TDataBase(TkTaskBase):
    parameterkeys = ['taskid', 'rundate']

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        # 加载mysql数据库配置
        self.begin_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.begin_time = time.time()
        self.date = self.get_param('rundate')
        self.taskid = self.get_param('taskid')
        self.config = TDataBaseConfig(self.taskid)
        # 日志参数
        self.len_source = 0
        self.len_target = 0
        self.update_number = 0
        self.delete_number = 0
        self.create_number = 0
        #数据加载的值
        self.source_data =None
        self.target_data = None
        #数据比较后的返回值
        self.create_datas = None
        self.delete_datas = None
        self.update_dict = {}

        self.ValidationObject = TValidationObject(self.taskid)

    def validate(self, value_list):
        self.ValidationObject.execute(value_list)

    def load_source_data(self):
        source_data = eval(self.config.sql)
        self.source_data = source_data
        return source_data

    @abstractmethod
    def load_target_data(self):  #不能全部加载源表，可能会有orm对象冲突，尤其是全量更新
        pass

    @abstractmethod
    def compare_data(self):
        pass

    @abstractmethod
    def update_and_delete(self):
        pass

    @abstractmethod
    def create_data(self):
        pass

    def update_save(self):
        if len(self.update_dict) > 0:
            for k,v in self.update_dict.items():
                for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
                    if hasattr(v, key):
                        setattr(k, key, getattr(v, key))
                k.vc_md5 = hashlib.md5(str(v).encode(encoding='UTF-8')).hexdigest()
            self.config.conn_target.save()

    @abstractmethod
    def delete_save(self):
        pass

    @abstractmethod
    def create_save(self):
        pass

    def save_datas(self):
        self.update_save()
        self.delete_save()
        self.create_save()

    def write_log(self):

        self.config.conn_mysql.execute_ext(
            "update t_status set l_status = 2 where l_taskid = {} ".format(self.get_param('taskid')))  # 更改表格状态为运行完成
        end_time = time.time()
        update_time = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
        filed_names = [['源表名称', self.config.source_table_name], ['目标表名称', self.config.target_table_name],
                       ['源表总条数', self.len_source], ['目标表总条数', self.len_target], ['增加条数', self.create_number],
                       ['修改条数', self.update_number], ['删除条数', self.delete_number],
                       ['运行时间', '{}分钟{}秒'.format((end_time - self.begin_time) // 60,
                                                 str((end_time - self.begin_time) % 60)[:4])],
                       ['开始时间', self.begin_time_str],
                       ['结束时间', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))]]
        for filed_name in filed_names:
            self.config.conn_target.execute_ext(
                "insert into t_log_info(l_log_id,l_taskobject_id,l_log_level,vc_msg,vc_filed_name,d_updatetime) values(seq_id.nextval,{},1,'{}','{}',to_date('{}','yyyy/mm/dd hh24:mi:ss'))"
                    .format(self.taskid, filed_name[1], filed_name[0], update_time))
        self.config.conn_target.save()
        self.config.conn_target.close()
        self.config.conn_source.close()
        self.config.conn_mysql.close()

    def __del__(self):
        self.write_log()

    def run(self):
        target_data = self.load_target_data()
        if target_data is not None:
            self.len_target = len(target_data)
        self.len_source = len(self.load_source_data())
        self.compare_data()
        compare_data = self.update_and_delete()
        if compare_data is not None:
            self.delete_number = len(compare_data[0])
            self.update_number = len(compare_data[1])
            self.validate(compare_data[1])
        create_data = self.create_data()
        self.create_number = len(create_data)
        self.validate(create_data)
        self.save_datas()
        logger.info('{}抽取完成'.format(self.config.target_table_name))




class TOracleFlashBack(TDataBase):
    def compare(self):
        pass
