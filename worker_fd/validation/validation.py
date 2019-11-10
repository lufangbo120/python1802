import importlib
import json
import os
import redis

from TopSpeedData_Worker.connection import connect_mysql
from .customvalidator import CustomValidator
from TopSpeedData_Worker.connection.oracle import connect_target

from model.t_log_dqc import TLogDqc
from settings import logger


class TransferDataConfig(object):
    def __init__(self, taskid):
        # 加载mysql数据库中表名和orm类名
        self.conn_mysql = connect_mysql()
        self.target_table_name = None
        self.load_const(taskid)

    def load_const(self, taskid):
        data = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(taskid))[
            0]  # 读取mysql所有配置
        self.target_table_name = data[4]  # 目标表名


class TValidationObject(TransferDataConfig):
    def __init__(self, taskid):
        TransferDataConfig.__init__(self,taskid)
        self.rule_expression = None
        self.taskid = taskid
        self.rulePath = 'validation/data.json'  # ../表示上一级目录
        self.extract_validaterules

    @property
    def rulePath(self):
        return self._rulePath

    @rulePath.setter
    def rulePath(self, value):
        if os.path.exists(value):  #判断文件路径是否存在
            self._rulePath = value
        else:
            self._rulePath = value
            logger.info("{}文件不存在".format(value))

    @property
    def extract_validaterules(self):
        # 校验规则读取
        with open(self.rulePath, 'r') as f:
            file_data = json.load(f)
            if str(self.taskid) in file_data.keys():
                if self.target_table_name == 't_bsc_investment_advice':
                    self.rule_expression = CustomValidator(file_data[str(self.taskid)],'t_tmp_bsc_investment_advice')
                else:
                    self.rule_expression = CustomValidator(file_data[str(self.taskid)],self.target_table_name)
                self.rule_expression.allow_unknown = True

    def execute(self, datalist):
        '''
        执行校验逻辑
        :param datalist:
        :return:
        '''
        if self.rule_expression is not None:
            logger.info("数据校验开始")
            insert_data = []
            for value in datalist:
                result = self.rule_expression.validate(value.__dict__)
                if not result:
                    for i in self.rule_expression.errors:
                        target = TLogDqc()
                        target.l_kind = 1
                        target.vc_msg = self.rule_expression.errors[i][0]
                        target.vc_target_table = self.target_table_name
                        target.vc_col_code = i
                        target.l_task_id = self.taskid
                        target.l_object_id = -1
                        if hasattr(value,'vc_md5'):
                            logger.info('vc_md5为{}的债券有错误{}'.format(value.vc_md5, self.rule_expression.errors))
                            target.vc_query_sql = 'select * from {0} where vc_md5 = {1}'.format(
                                self.target_table_name, value.vc_md5)
                        else:
                            logger.info('vc_sname为{}的债券有错误{}'.format(value.vc_sname, self.rule_expression.errors))
                            target.vc_query_sql = 'select * from {0} where vc_sname = {1}'.format(
                                self.target_table_name, value.vc_sname)
                        insert_data.append(target)
            self.write_validation_log(insert_data)
            logger.info("数据校验结束")
        else:
            logger.info("未配置校验规则")

    def write_validation_log(self, insert_data):
        '''
        校验日志写入数据库
        :param result:
        :return:
        '''
        conn_target = connect_target()
        conn_target.add_all(insert_data)

        conn_target.close()

