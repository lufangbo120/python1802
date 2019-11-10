import datetime

from data_extract.t_data_md5 import TDataMD5
from data_extract.t_globle_data import TGlobleData
from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TInstruction(TGlobleData):
    def __init__(self,param):
        super(TInstruction, self).__init__(param)  # 多继承
        self.begindate = None
        self.enddate = None
        self.portcode = None

    def create_data(self):
        insert_data = []
        for data in self.source_data:
            target = self.config.target_orm_name()  # 对象必须每次都创建一个，不然只会增加一个对象。
            target.__dict__.update(data)
            #for key in self.config.source_orm_name.__mapper__.tables[0].columns._data:
               # if hasattr(data, key):
                   # setattr(target, key, getattr(data, key))
            target.vc_source = 'pas'
            target.d_updatetime = datetime.datetime.now()
            insert_data.append(target)
        self.create_datas = insert_data
        logger.debug('{}增加{}条'.format(self.config.target_table_name, len(insert_data)))
        return insert_data

    def run(self):
        for i in range(len(self.get_param('begindate'))):
            self.begindate = self.get_param('begindate')[i]
            self.enddate = self.get_param('enddate')[i]
            self.portcode = self.get_param("portcode")[i]
            super().run()

regiest_task("TInstruction", TInstruction)
