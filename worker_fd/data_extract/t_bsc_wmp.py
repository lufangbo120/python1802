import hashlib

from extract_base.t_data_base import CONST_SEPARATOR
from data_extract.t_data_md5 import TDataMD5
from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TBscWmp(TDataMD5):

    def update_save(self):
        dict_data = self.config.conn_mysql.execute("select * from t_dictionary where l_dictionary_no = 10010")
        if len(self.update_dict) > 0:
            for k,v in self.update_dict.items():
                for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
                    if hasattr(v, key):
                        setattr(k, key, getattr(v, key))
                for i in dict_data:
                    if i.vc_item_name == v.vc_risk_type:
                        k.vc_risk_type = i.vc_lemma_item
                k.vc_md5 = hashlib.md5(str(v).encode(encoding='UTF-8')).hexdigest()
            self.config.conn_target.save()

    def create_data(self):
        # 增加数据
        dict_data = self.config.conn_mysql.execute("select * from t_dictionary where l_dictionary_no = 10010")
        insert_data = []
        for source_diff in self.source_diffs:
            source_diff = source_diff.split(CONST_SEPARATOR)
            if self._target_dict_data.get(source_diff[0]) == None :
                target = self.config.target_orm_name()  # 对象必须每次都创建一个，不然只会增加一个对象。
                target.__dict__.update(self._source_dict_data[source_diff[0]])
                target.vc_md5 = self.get_hash(self._source_dict_data[source_diff[0]])
                for i in dict_data:
                    if i.vc_item_name == self._source_dict_data[source_diff[0]].vc_risk_type:
                        target.vc_risk_type = i.vc_lemma_item
                insert_data.append(target)  # 可以给源表单独加一个vc_md5的属性，然后查源表
        self.create_datas = insert_data
        self.create_number = len(insert_data)
        logger.info('{}增加{}条'.format(self.config.target_table_name, len(insert_data)))
        return insert_data


regiest_task('TBscWmp',TBscWmp)
