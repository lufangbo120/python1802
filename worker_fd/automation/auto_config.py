import cx_Oracle
from TopSpeedData_Worker.connection import connect_mysql
from TopSpeedData_Worker.connection.oracle import engine_source
from settings import MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME, logger
import pandas as pd

class TAutoConfig(object):

    def __init__(self,id,target_name,source_name):
        self.id = id
        self.target_name = target_name.lower()
        self.source_name = source_name.lower()
        self.tar_orm_name = None
        self.sou_orm_name = None
        self.sql = None

    def cre_tar_orm_name(self):
        tar_orm_name = ''
        target_name = self.target_name.split('_')
        for i in target_name:
            tar_orm_name +=  i.capitalize()
        self.tar_orm_name = tar_orm_name
        logger.info("目标表orm为{}".format(tar_orm_name))

    def cre_sou_orm_name(self):
        sou_orm_name = ''
        source_name = self.source_name.split('_')
        for i in source_name:
            sou_orm_name +=  i.capitalize()
        self.sou_orm_name = sou_orm_name
        logger.info("目标表orm为{}".format(sou_orm_name))

    def cre_sql(self):
        df1 = pd.read_sql('select * from hs_trade.{} where rownum < 5'.format(self.source_name), engine_source)
        column_list = df1.columns.values.tolist()
        columns = ''
        for i in column_list:
            columns += i
            columns += ','
        columns = columns.rstrip(',')
        sql = "self.config.conn_source.execute('select {0} from hs_trade.{1}')".format(columns, self.source_name)
        self.sql = sql
        logger.info("生成的sql为{}".format(sql))

    def save_db(self):
        db = connect_mysql()
        db.execute_ext(
            'insert into t_extract_config(l_task_id,vc_souce_orm_name,vc_target_orm_name,vc_souce_table_name,vc_target_table_name,vc_source,l_auto_model,vc_sql) VALUES ("{}","{}","{}","{}","{}",10,1,"{}")'.format(
                self.id, self.sou_orm_name, self.tar_orm_name, self.source_name, self.target_name,self.sql))
        db.execute_ext(
            "insert into t_task_info(id,vc_task_name,l_visble,l_type,vc_operator,l_priority,vc_remark,vc_trigger_type ,l_bus_type) VALUES ('{}','{}',1,490,'卢方波',0,'基础数据抽取',1,1)".format(
                self.id, self.target_name))
        db.save()
    
    def call_pro(self):
        try:
            conn = cx_Oracle.connect(
                '{}/{}@{}/{}'.format(MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME))
            cursor = conn.cursor()
            cursor.callproc("p_create_table", [self.source_name, self.target_name])
            cursor.close()
            conn.close()
            logger.info('存储过程执行完成')
        except Exception as e:
            logger.info("存储过程异常{}".format(e))


            
    def run(self):
        self.cre_tar_orm_name()
        self.cre_sou_orm_name()
        self.cre_sql()
        self.save_db()
        self.call_pro()
      
obj =   TAutoConfig(773,'t_bsc_ibmminfo','dm_bsc_ibmminfo')
obj.run()
      
      
           
