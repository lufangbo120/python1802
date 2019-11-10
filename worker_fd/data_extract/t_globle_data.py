from extract_base.t_data_base import TDataBase
from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TGlobleData(TDataBase):

    def load_target_data(self):
        pass

    def compare_data(self):
        pass

    def update_and_delete(self):
        pass

    def delete_save(self):
        eval(self.config.sql1)
        self.config.conn_target.save()

    def create_save(self):
        if len(self.create_datas) > 0:  # 增加数据
            self.config.conn_target._add_all(self.create_datas)



    def create_data(self):
        insert_data = []
        for i in self.source_data:
            target = self.config.target_orm_name()  # 对象必须每次都创建一个，不然只会增加一个对象。
            for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
                if hasattr(i, key):
                    setattr(target, key, getattr(i, key))
            insert_data.append(target)  # 可以给源表单独加一个vc_md5的属性，然后查源表
        self.create_datas = insert_data
        logger.info('{}增加{}条'.format(self.config.target_table_name, len(insert_data)))
        return insert_data


regiest_task("TGlobleData", TGlobleData)
