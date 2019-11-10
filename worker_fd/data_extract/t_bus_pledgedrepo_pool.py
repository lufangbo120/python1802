from extract_base.t_data_base import TDataBase, CONST_SEPARATOR
from data_extract.t_data_md5 import TDataMD5

from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TBusPledgedrepoPool(TDataMD5):

    def create_data(self):
        insert_data = []
        for source_diff in self.source_diffs:
            source_diff = source_diff.split(CONST_SEPARATOR)
            if self._target_dict_data.get(source_diff[0]) == None:
                target = self.config.target_orm_name()  # 对象必须每次都创建一个，不然只会增加一个对象。
                for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
                    if hasattr(self._source_dict_data[source_diff[0]], key):
                        setattr(target, key,
                                getattr(self._source_dict_data[source_diff[0]], key))  # 通过md5的位数用切片切出MD5，减少for循环的次数
                    target.vc_md5 = self.get_hash(self._source_dict_data[source_diff[0]])
                    if getattr(self._source_dict_data[source_diff[0]], 'l_market') == 1:
                        target.vc_scode = getattr(self._source_dict_data[source_diff[0]],
                                                  'vc_code') + 'SH'  # 证券交易所上海
                    if getattr(self._source_dict_data[source_diff[0]], 'l_market') == 2:
                        target.vc_scode = getattr(self._source_dict_data[source_diff[0]],
                                                  'vc_code') + 'SZ'  # 深圳证券交易所
                insert_data.append(target)  # 可以给源表单独加一个vc_md5的属性，然后查源表
        self.create_datas = insert_data
        logger.info('{}增加{}条'.format(self.config.target_table_name, len(insert_data)))
        self.config.conn_target.add_all(insert_data)
        return insert_data



regiest_task("TBusPledgedrepoPool", TBusPledgedrepoPool)
