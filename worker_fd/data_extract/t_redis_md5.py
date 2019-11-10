import hashlib
import time
import datetime
import numpy
import math

import redis

from extract_base.t_data_base import TDataBase, CONST_SEPARATOR
from data_extract.t_data_md5 import TDataMD5
from settings import logger, REDIS_HOST, REDIS_POST, REDIS_DB, REDIS_PASSWORD
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TRedisMD5(TDataMD5):
    def __init__(self, param):
        super(TRedisMD5, self).__init__(param)
        pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_POST, db=REDIS_DB, password=REDIS_PASSWORD, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)

    def load_target_data(self):
        target_data = self.r.hvals('{}'.format(self.config.target_table_name))
        self.target_data = target_data
        return target_data

    def update_save(self):
        if len(self.update_dict) > 0:
            records = []
            del_records = []
            for k,v in self.update_dict.items():
                del_records.append(k.vc_md5)
                for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
                    if hasattr(v, key):
                        setattr(k, key, getattr(v, key))
                k.vc_md5 = hashlib.md5(str(v).encode(encoding='UTF-8')).hexdigest()
                records.append(k)
            self.config.conn_target.save()
            self.r.hdel(self.config.target_table_name, *del_records)
            self.add_to_redis(records)

    def create_save(self):
        if len(self.create_datas) > 0:  # 增加数据
            self.config.conn_target.add_all(self.create_datas)
            self.add_to_redis(self.create_datas)    #redis增加数据

    def add_to_redis(self,records):
        if len(records) == 0:
            return

        post_count = 200000
        record_count = len(records)
        post = math.ceil(record_count / post_count)

        for i in range(post):
            begin_index = i * post_count
            if i + 2 <= post:
                end_index = (i + 1) * post_count
            else:
                end_index = record_count
            tar_dict = {}
            for i in records[begin_index:end_index]:
                tar_dict[i.vc_md5] = i  # redis存储orm对象，会直接存成字符串
            self.r.hmset(self.config.target_table_name,tar_dict)

    def delete_save(self):
        super().delete_save()
        if len(self.delete_datas) == 0:
            return
        self.r.hdel(self.config.target_table_name, *self.delete_datas)  #redis删除数据


regiest_task("TRedisMD5", TRedisMD5)
