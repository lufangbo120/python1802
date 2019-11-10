from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase, regiest_task
from settings import MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME
from settings import logger
import cx_Oracle
from TopSpeedData_Worker.connection import connect_mysql
from TopSpeedData_Worker.connection.oracle import connect_source, connect_target
from model import TStatus
from pypinyin import pinyin,lazy_pinyin,Style
import re

class CallPortData(TkTaskBase):
    parameterkeys = ["taskid"]

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        self.task_id = self.get_param("taskid")

    def rows_as_dicts(self,cursor):
        col_names = [i[0] for i in cursor.description]
        return [dict(zip(col_names, row)) for row in cursor]

    def Topinyin(self,table, key, target, sql1, sql2):
        logger.info('连接数据库')
        conn = cx_Oracle.connect(
            '{}/{}@{}/{}'.format(MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME))
        cursor = conn.cursor()
        # 读取目标表
        cursor.execute(sql1)
        rows = self.rows_as_dicts(cursor)
        logger.info('获取更新记录')
        for row in rows:
            # 获取主键及目标字段名称
            primary_key = str(row['%s' % key])
            target_col = row['%s' % target]
            # 获取简称中中文
            target_col = re.findall("[\u4e00-\u9fa5]+", str(target_col))
            # 获得简称英文首字母
            dic = pinyin(target_col, style=Style.FIRST_LETTER)
            # 拼接英文简称
            vc_spell = ''.join(str(i[0]) for i in dic).upper()
            # 根据主键更新拼音简称
            sql = sql2.format(vc_spell, primary_key)
            cursor.execute(sql)
            cursor.execute("commit")
        logger.info('%s简称更新结束' % table)
        cursor.close()
        conn.close()

    def Update_py(self):
        # 更新账户拼音简称
        table = 't_port_fund_info'
        sql1 = "select * from t_port_fund_info a where  a.vc_fund_name_en is null"
        key = 'L_FUND_ID'
        target = 'VC_FUND_NAME'
        sql2 = 'UPDATE t_port_fund_info SET vc_fund_name_en =  \'{0}\' where l_fund_id = \'{1}\''
        self.Topinyin(table, key, target, sql1, sql2)
        # 更新资产单元拼音简称
        table = 't_port_asset_info'
        sql1 = "select * from t_port_asset_info a where  a.vc_asset_name_en is null"
        key = 'L_ASSET_ID'
        target = 'VC_ASSET_NAME'
        sql2 = 'UPDATE t_port_asset_info SET vc_asset_name_en =  \'{0}\' where l_asset_id = \'{1}\''
        self.Topinyin(table, key, target, sql1, sql2)
        # 更新组合拼音简称
        table = 't_port_combi_info'
        sql1 = "select * from t_port_combi_info a where  a.vc_combi_name_en is null"
        key = 'L_COMBI_ID'
        target = 'VC_COMBI_NAME'
        sql2 = 'UPDATE t_port_combi_info SET vc_combi_name_en =  \'{0}\' where l_combi_id = \'{1}\''
        self.Topinyin(table, key, target, sql1, sql2)

    def call_port_data(self):
        logger.info('开始执行存储过程')
        dbsession_my = connect_mysql()
        # dbsession_md = connect_target()
        try:
            logger.info('开始执行存储过程')
            logger.info('连接数据库')
            conn = cx_Oracle.connect('{}/{}@{}/{}'.format(MD_SERVER_USER,MD_SERVER_PASS,MD_SERVER_ADDRESS,MD_SERVICE_NAME))
            cursor = conn.cursor()
            logger.info('存储过程正在执行，请等待...')
            cursor.callproc('p_update_port_asset_info')
            cursor.callproc('p_update_port_combi_info')
            cursor.callproc('p_update_port_fund_info')
            cursor.callproc('p_update_port_fund_equity')
            cursor.callproc('p_update_port_fund_fixincome')
            cursor.callproc('p_update_port_map_common')
            cursor.callproc('p_update_port_o3_map_dept')
            cursor.callproc('p_update_port_o3_map_manager')
            self.Update_py()
            logger.info('存储过程执行完成')
            cursor.close()
            conn.close()
            dbsession_my.query(TStatus).filter(TStatus.l_child_id == self.task_id).update({TStatus.l_status: 0})
            dbsession_my.close()
            logger.info('存储过程执行完成')
        except Exception as e:
            print('{}'.format(e))
            logger.info('存储过程执行异常，请检查')
        finally:
             pass

    def run(self):
        self.call_port_data()

regiest_task("CallPortData", CallPortData)

