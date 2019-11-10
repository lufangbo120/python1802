import hashlib
import time
import datetime
import numpy
import math
from extract_base.t_data_base import TDataBase, CONST_SEPARATOR
# from model.t_md5s import TMd5
from model.t_md5s import TMd5
from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TDataMD5(TDataBase):
    def __init__(self, param):
        super(TDataMD5, self).__init__(param)
        # 对比产生的不同值
        self.target_diffs = None
        self.source_diffs = None
        # 私有属性
        self._source_dict_data = None
        self._target_dict_data = None
        self._source_keys = None
        self._target_keys = None
      

    def get_hash(self, record):
        return hashlib.md5(str(record).encode(encoding='UTF-8')).hexdigest()

    def load_target_data(self):
        if self.config.update_date == 0:  # 0代表不按时间更新
            target_data = self.config.conn_target.query(self.config.target_orm_name).all()
            self.target_data = target_data
            return target_data
        elif self.config.update_date == 1:  # 1代表按照今天的时间进行更新
            target_data = eval(self.config.vc_orm)
            self.target_data = target_data
            return target_data

    def compare_data(self):#源表数据和目标表数据
        list_source = []
        list_target = []
        dict_source = {}
        dict_target = {}
        logger.info('源表{}数据{}条'.format(self.config.source_table_name, len(self.source_data)))
        if isinstance(self.source_data, list):
            source_object = self.config.source_orm_name()
            source_object = str(source_object).split(CONST_SEPARATOR)
            while self.source_data:
                source = self.source_data.pop()
                key = ''
                for i in source_object:
                    key += str(source[i])
                dict_source[key] = source  # source的串必须拼全部，不然无法生成所有字段的md5的值
                list_source.append(key + CONST_SEPARATOR + self.get_hash(source))
        logger.info('目标表{}数据{}条'.format(self.config.target_table_name, len(self.target_data)))
        if isinstance(self.target_data, list):
            while self.target_data:
                target = self.target_data.pop()
                list_target.append(str(target))
                dict_target[str(target).split(CONST_SEPARATOR)[0]] = target
        numpy_sources = numpy.array(list_source)
        numpy_targets = numpy.array(list_target)
        self.target_diffs = numpy.setdiff1d(numpy_targets, numpy_sources)
        self.source_diffs = numpy.setdiff1d(numpy_sources, numpy_targets)
        self._source_dict_data = dict_source
        self._target_dict_data = dict_target

    # def update_and_delete(self):
    #     target_md5s = []
    #     for target_diff in self.target_diffs:
    #         target = target_diff.split(CONST_SEPARATOR)
    #         if self._source_dict_data.get(target[0]) != None:
    #             source = self._source_dict_data[target[0]]
    #             # tesd_data = self._target_dict_data.get(target[0])
    #             tesd_data = self.get_tesd_target()
    #             self.update_dict[tesd_data] = source
    #         else:
    #             target_md5s.append(target[-1])
    #     self.delete_datas = target_md5s
    #     logger.info('{}修改{}条'.format(self.config.target_table_name, len(self.update_dict)))
    #     logger.info('{}删除{}条'.format(self.config.target_table_name, len(target_md5s)))
    #     return target_md5s,self.update_dict

    def update_and_delete(self):
        target_md5s = []
        value = []
        for target_diff in self.target_diffs:
            target = target_diff.split(CONST_SEPARATOR)
            value.append(target[-1])
        target_diffs = self.get_tesd_target(value)
        for target_diff in target_diffs:
            target = str(target_diff).split(CONST_SEPARATOR)
            if self._source_dict_data.get(target[0]) != None:
                source = self._source_dict_data[target[0]]
                tesd_data = target_diff
                self.update_dict[tesd_data] = source
            else:
                target_md5s.append(target[-1])
        self.delete_datas = target_md5s
        logger.info('{}修改{}条'.format(self.config.target_table_name, len(self.update_dict)))
        logger.info('{}删除{}条'.format(self.config.target_table_name, len(target_md5s)))
        return target_md5s, self.update_dict

    def get_tesd_target(self,value):
        records = value
        if len(records) == 0:
            return []
        post_count = 1000  # oracle更新和删除操作一次最多支持1000条，除非用子查询
        record_count = len(records)
        tesd_target = []
        post = math.ceil(record_count / post_count)
        for i in range(post):
            begin_index = i * post_count
            if i + 2 <= post:
                end_index = (i + 1) * post_count
            else:  # 最后一次循环走这里
                end_index = record_count
            data = self.config.conn_target.query(self.config.target_orm_name).filter(self.config.target_orm_name.vc_md5.in_(records[begin_index:end_index])).all()
            tesd_target += data

        return tesd_target


    def create_data(self):
        # 增加数据
        insert_data = []
        for source_diff in self.source_diffs:
            source_diff = source_diff.split(CONST_SEPARATOR)
            if self._target_dict_data.get(source_diff[0]) == None :
                target = self.config.target_orm_name()  # 对象必须每次都创建一个，不然只会增加一个对象。
                target.__dict__.update(self._source_dict_data[source_diff[0]])
                target.vc_md5 = self.get_hash(self._source_dict_data[source_diff[0]])
                insert_data.append(target)  # 可以给源表单独加一个vc_md5的属性，然后查源表
        self.create_datas = insert_data
        self.create_number = len(insert_data)
        logger.info('{}增加{}条'.format(self.config.target_table_name, len(insert_data)))
        return insert_data

    def create_save(self):
        if len(self.create_datas) > 0:  # 增加数据
            self.config.conn_target.add_all(self.create_datas)

    def delete_save(self):
        records = self.delete_datas
        if len(records) == 0:
            return
        post_count = 1000   #oracle更新和删除操作一次最多支持1000条，除非用子查询
        record_count = len(records)
        post = math.ceil(record_count / post_count)
        rushu = None
        for i in range(post):
            begin_index = i * post_count
            if i + 2 <= post:
                end_index = (i + 1) * post_count
            else:  # 最后一次循环走这里
                end_index = record_count
                rushu = end_index % post_count
            if rushu == 1: #在集合中只有一条数据会报错，oracle不支持带逗号的元祖。
                self.config.conn_target.execute_ext(
                    "update {0} set l_delete = 1 where vc_md5 = '{1}' and vc_update_operater is null".format(self.config.target_table_name,
                                                                  records[begin_index:begin_index + 1][0]))

            else:
                self.config.conn_target.execute_ext(
                    'update {0} set l_delete = 1 where vc_md5 in {1} and vc_update_operater is null'.format(self.config.target_table_name,
                                                                 tuple(records[begin_index:end_index])))
        self.config.conn_target.save()

    def save_to_mysql(self):
        datas = []
        cre_datas = []
        up_datas = []
        del_datas = []
        self.config.conn_target.execute_ext("delete from t_md5s where vc_table_name = '{}'".format(self.config.target_table_name))
        self.config.conn_target.save()
        for i in self.create_datas:
            target = TMd5()
            target.vc_table_name = self.config.target_table_name
            target.l_status = 1
            target.vc_md5 = i.vc_md5
            cre_datas.append(target)
        # self.config.conn_target.add_all(cre_datas)
        for i in self.update_dict:
            target = TMd5()
            target.vc_table_name = self.config.target_table_name
            target.l_status = 2
            target.vc_md5 = i.vc_md5
            up_datas.append(target)
        # self.config.conn_target.add_all(up_datas)
        for i in self.delete_datas:
            target = TMd5()
            target.vc_table_name = self.config.target_table_name
            target.l_status = 3
            target.vc_md5 = i
            del_datas.append(target)
        datas = cre_datas + up_datas + del_datas
        self.config.conn_target.add_all(datas)
        cre_sql = "select * from {0} where vc_md5 in (select vc_md5 from t_md5s where vc_table_name = {0} and l_status = 1)".format(self.config.target_table_name)
        up_sql = "select * from {0} where vc_md5 in (select vc_md5 from t_md5s where vc_table_name = {0} and l_status = 2)".format(self.config.target_table_name)
        del_sql = "select * from {0} where vc_md5 in (select vc_md5 from t_md5s where vc_table_name = {0} and l_status = 3)".format(self.config.target_table_name)
        self.config.conn_mysql.execute_ext(
            "delete from t_mess_info where id = {}".format(self.taskid))
        self.config.conn_mysql.execute_ext("insert into t_mess_info(id,vc_task_name,l_send,vc_cre_sql,vc_up_sql,vc_del_sql)"
                                           " values('{}','{}',1,'{}','{}','{}')".format(self.taskid,self.config.target_table_name,cre_sql,up_sql,del_sql))


    def run(self):
        super().run()
        self.save_to_mysql()


regiest_task("TDataMD5", TDataMD5)
