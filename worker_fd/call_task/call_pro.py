# from connection.oracle import connect_target
from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase, regiest_task
from settings import MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME
from settings import logger
import cx_Oracle
from TopSpeedData_Worker.connection import connect_mysql
from TopSpeedData_Worker.connection.oracle import connect_source, connect_target
from model import TStatus
from pypinyin import pinyin,lazy_pinyin,Style
import re

class CallProducer(TkTaskBase):
    parameterkeys = ["taskid"]

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        self.task_id = self.get_param("taskid")

    def rows_as_dicts(self,cursor):
        col_names = [i[0] for i in cursor.description]
        return [dict(zip(col_names, row)) for row in cursor]

    def Update_py(self):
            logger.info('连接数据库')
            conn = cx_Oracle.connect('{}/{}@{}/{}'.format(MD_SERVER_USER,MD_SERVER_PASS,MD_SERVER_ADDRESS,MD_SERVICE_NAME))
            cursor = conn.cursor()
            logger.info('开始更新表t_bsc_security证券简称英文字段')
            cursor.execute(
                "select * from t_bsc_security a where  a.vc_sname is not null and a.vc_spell_abbr is null and a.vc_source = 'MD'")
            rows = self.rows_as_dicts(cursor)
            logger.info('获取更新记录')
            for row in rows:
                # 获取证券内码
                #logger.info('获取证券内码')
                vc_scode = str(row['VC_SCODE'])
                vc_sname = row['VC_SNAME']
                # 获取简称中中文
                # vc_name = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", str(vc_sname))
                vc_name = re.findall("[\u4e00-\u9fa5]+", str(vc_sname))
                # 获得简称英文首字母
                dic = pinyin(vc_name, style=Style.FIRST_LETTER)
                # 拼接英文简称
                #logger.info('拼接英文简称')
                vc_spell = ''.join(str(i[0]) for i in dic).upper()
                #logger.info('开始更新表t_bsc_security证券简称英文字段')
                sql = 'UPDATE t_bsc_security SET VC_SPELL_ABBR =  \'{0}\' where vc_scode = \'{1}\''.format(vc_spell,vc_scode)
                # print(sql)
                cursor.execute(sql)
                cursor.execute("commit")
                #logger.info('开始更新表t_bsc_security证券简称更新结束')
            cursor.close()
            conn.close()

    def Call_pro(self):
        logger.info('开始执行存储过程')
        dbsession_my = connect_mysql()
        # dbsession_md = connect_target()
        try:
            #logger.info('开始执行存储过程')
            logger.info('连接数据库')
            conn = cx_Oracle.connect('{}/{}@{}/{}'.format(MD_SERVER_USER,MD_SERVER_PASS,MD_SERVER_ADDRESS,MD_SERVICE_NAME))
            cursor = conn.cursor()
            logger.info('存储过程PKG_BSC_SECURITY正在执行，请等待...')
            cursor.callproc('PKG_BSC_SECURITY.P_UPDATE_TMP_BSC_SECURITY')
            cursor.callproc('PKG_BSC_SECURITY.P_UPDATE_TL4')
            cursor.callproc('PKG_BSC_SECURITY.P_UPDATE_KIND_ATYPE')
            cursor.callproc('PKG_BSC_SECURITY.P_UPDATE_BSC_SECURITY')
            cursor.callproc('p_update_residual_maturity')
            cursor.callproc('p_update_bsc_marketinfo')
            self.Update_py()
            #logger.info('存储过程执行完成')
            cursor.close()
            conn.close()
            dbsession_my.query(TStatus).filter(TStatus.l_child_id == self.task_id).update({TStatus.l_status: 0})
            dbsession_my.close()
            logger.info('存储过程执行完成')
        except Exception as e:
            #print('{}'.format(e))
            logger.info('存储过程执行异常，请检查')
        finally:
             pass

    def run(self):
        self.Call_pro()

regiest_task("CallProducer", CallProducer)

