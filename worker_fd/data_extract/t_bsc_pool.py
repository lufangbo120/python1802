import cx_Oracle
import os

from dbfread import DBF
from simpledbf import Dbf5
import pandas as pd
import os
import time
import shutil

from TopSpeedData_Worker.connection.oracle import connect_target
from model.t_tmp_bsc_pooldata_dbf import TTmpBscPooldataDbf
from model.t_tmp_bsc_pooldata_reason import TTmpBscPooldataReason
from model.t_tmp_bsc_pooldata_xls import TTmpBscPooldataXl
from settings import logger, MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME
from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase, regiest_task


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 设置字符集，防止中文乱码

#TODAY = time.strftime('%Y%m%d', time.localtime(time.time()))
#PATH1 = r'/home/tkamc/file/caihuiDBF/{}'.format(TODAY)     #财汇路径
#PATH2 = r'/home/tkamc/file/touyan/{}'.format(TODAY)    #投研路径
#PATH3 = r'/home/tkamc/file/file_csv/{}'.format(TODAY)    #存储位置
class ExtractPool(TkTaskBase):

    parameterkeys = ['taskid','rundate']

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        #加载mysql数据库配置
        taskid = self.get_param('taskid')
        global TODAY,PATH1,PATH2,PATH3,TODAY1
        TODAY = self.get_param('rundate')
        st = str(TODAY)
        TODAY1 = st[:4]+'-'+st[4:6]+'-'+st[6:]
        PATH1 = r'/home/tkamc/file/caihuiDBF/{}'.format(TODAY)     #财汇路径
        PATH2 = r'/home/tkamc/file/touyan/{}'.format(TODAY)    #投研路径
        PATH3 = r'/home/tkamc/file/file_csv/{}'.format(TODAY)    #存储位置

        self.conn_target = connect_target()
        self.csv_name = []
        self.csv_name_xls = []
        self.name5 = None
        self.name4 = None
        logger.info("开始复制文件")
        self.copy_to_dir()
        logger.info("文件复制完成") 

    def copy_to_dir(self):
        PATH = [PATH1,PATH2,PATH3]
        for i in PATH:
            if not os.path.exists(i):
                os.mkdir(i)
        S_PATH1 = [r'/caihuiDBF/DBF/{}/gics一级分类{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH2 = [r'/caihuiDBF/DBF/{}/保险组定制{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH3 = [r'/caihuiDBF/DBF/{}/股票维度{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH4 = [r'/caihuiDBF/DBF/{}/基金池{}.DBF'.format(TODAY,TODAY) ,r'{}'.format(PATH1)]
        S_PATH5 = [r'/caihuiDBF/DBF/{}/年金维度池{}.DBF'.format(TODAY,TODAY) ,r'{}'.format(PATH1)]
        S_PATH6 = [r'/caihuiDBF/DBF/{}/年金维度池B{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH7 = [r'/caihuiDBF/DBF/{}/年金维度池C{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH8 = [r'/caihuiDBF/DBF/{}/年金维度池D{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH9 = [r'/caihuiDBF/DBF/{}/年金维度池E{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH10 = [r'/caihuiDBF/DBF/{}/年金维度池F{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH11 = [r'/caihuiDBF/DBF/{}/企业年金禁限投证券{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH12 = [r'/caihuiDBF/DBF/{}/申万行业三级分类{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH13 = [r'/caihuiDBF/DBF/{}/债券维度{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH14 = [r'/caihuiDBF/DBF/{}/证监会一级行业分类{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH15 = [r'/caihuiDBF/DBF/{}/专户风控{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH16 = [r'/caihuiDBF/DBF/{}/专户风控2{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH17 = [r'/caihuiDBF/DBF/{}/专户风控3{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH18 = [r'/caihuiDBF/DBF/{}/专户风控4{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH19 = [r'/caihuiDBF/DBF/{}/资管产品风控{}.DBF'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH20 = [r'/caihuiDBF/DBF/{}/债券禁选池原因{}.xls'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH21 = [r'/caihuiDBF/DBF/{}/PAR_PISTOCK_INFO{}.xls'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH22 = [r'/caihuiDBF/行业数据/{}/行业数据{}.xls'.format(TODAY,TODAY),r'{}'.format(PATH1)]
        S_PATH23 = [r'/touyan/{}/信用债二级库备选库.xls'.format(TODAY1),r'{}'.format(PATH2)]
        S_PATH24 = [r'/touyan/{}/消费服务备选库.xls'.format(TODAY1),r'{}'.format(PATH2)]
        S_PATH25 = [r'/touyan/{}/BB-库.xls'.format(TODAY1),r'{}'.format(PATH2)]
        S_PATH26 = [r'/touyan/{}/信用风险债券池.xls'.format(TODAY1),r'{}'.format(PATH2)]
        S_PATH27 = [r'/touyan_hangyezuhe/StockIndustry{}.xls'.format(TODAY),r'{}'.format(PATH2)]
        S_PATH = [S_PATH1,S_PATH2,S_PATH3,S_PATH4,S_PATH5,S_PATH6,S_PATH7,S_PATH8,S_PATH9,S_PATH10,S_PATH11,S_PATH12,S_PATH13,S_PATH14,S_PATH15,S_PATH16,S_PATH17,S_PATH18,S_PATH19,S_PATH20,S_PATH21,S_PATH22,S_PATH23,S_PATH24,S_PATH25,S_PATH26,S_PATH27]
        for i in S_PATH:
            shutil.copy( i[0], i[1])

   
    def dbf2csv(self):
        try:
            name0=  [r"{}/gics一级分类{}.DBF".format(PATH1,TODAY),r"{}/GICSYJFL{}.csv".format(PATH3,TODAY)]
            name1=  [r"{}/保险组定制{}.DBF".format(PATH1,TODAY),r"{}/BXZDZ{}.csv".format(PATH3,TODAY)]
            name2=  [r"{}/股票维度{}.DBF".format(PATH1,TODAY),r"{}/GPWD{}.csv".format(PATH3,TODAY)]
            name3=  [r"{}/基金池{}.DBF".format(PATH1,TODAY),r"{}/JJC{}.csv".format(PATH3,TODAY)]
            name4=  [r"{}/年金维度池{}.DBF".format(PATH1,TODAY),r"{}/NJWDC{}.csv".format(PATH3,TODAY)]
            name5=  [r"{}/年金维度池D{}.DBF".format(PATH1,TODAY),r"{}/NJWDCD{}.csv".format(PATH3,TODAY)]
            name6=  [r"{}/年金维度池E{}.DBF".format(PATH1,TODAY),r"{}/NJWDCE{}.csv".format(PATH3,TODAY)]
            name7=  [r"{}/年金维度池F{}.DBF".format(PATH1,TODAY),r"{}/NJWDCF{}.csv".format(PATH3,TODAY)]
            name8=  [r"{}/专户风控2{}.DBF".format(PATH1,TODAY),r"{}/ZHFK2{}.csv".format(PATH3,TODAY)]
            name9=  [r"{}/专户风控3{}.DBF".format(PATH1,TODAY),r"{}/ZHFK3{}.csv".format(PATH3,TODAY)]
            name10=  [r"{}/资管产品风控{}.DBF".format(PATH1,TODAY),r"{}/ZGCPFK{}.csv".format(PATH3,TODAY)]
            name11=  [r"{}/专户风控{}.DBF".format(PATH1,TODAY),r"{}/ZHFK{}.csv".format(PATH3,TODAY)]
            name12=  [r"{}/专户风控4{}.DBF".format(PATH1,TODAY),r"{}/ZHFK4{}.csv".format(PATH3,TODAY)]
            name13=  [r"{}/年金维度池B{}.DBF".format(PATH1,TODAY),r"{}/NJWDCB{}.csv".format(PATH3,TODAY)]
            name14=  [r"{}/年金维度池C{}.DBF".format(PATH1,TODAY),r"{}/NJWDCC{}.csv".format(PATH3,TODAY)]
            name15=  [r"{}/企业年金禁限投证券{}.DBF".format(PATH1,TODAY),r"{}/QYNJJXTZQ{}.csv".format(PATH3,TODAY)]
            name16=  [r"{}/申万行业三级分类{}.DBF".format(PATH1,TODAY),r"{}/SWHYSJFL{}.csv".format(PATH3,TODAY)]
            name17=  [r"{}/债券维度{}.DBF".format(PATH1,TODAY),r"{}/ZQWD{}.csv".format(PATH3,TODAY)]
            name18=  [r"{}/证监会一级行业分类{}.DBF".format(PATH1,TODAY),r"{}/ZJHYJHYFL{}.csv".format(PATH3,TODAY)]
            self.name4 = name4
            names = [name0,name1,name2,name3,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18]  
            for name in names:
                if os.path.exists(name[1]): #判断文件是否存在
                    os.remove(name[1])  #文件每次都要删除，不然会一直变大
                dbf_name = name[0]
                dbf = Dbf5(dbf_name,codec = 'gbk')
                csv_name = name[1]
                self.csv_name.append(csv_name)
                dbf.to_csv(csv_name)
        except Exception as err:
            logger.error("error: {0}".format(err))

    def xls2csv(self):
        # excel文件转csv
        name0 = [r"{}/行业数据{}.xls".format(PATH1,TODAY),r"{}/HYSJ{}.csv".format(PATH3,TODAY)]
        data = pd.read_excel(name0[0],converters={u'证券代码':str,u"CODE":str})
        data.to_csv(name0[1], encoding='gbk')
        name1 = [r"{}/StockIndustry{}.xls".format(PATH2,TODAY),r"{}/STOCKINDUSTRY{}.csv".format(PATH3,TODAY)]
        name2 = [r"{}/消费服务备选库.xls".format(PATH2),r"{}/XFFWBXK{}.csv".format(PATH3,TODAY)]
        name3 = [r"{}/信用风险债券池.xls".format(PATH2),r"{}/XYFXZQC{}.csv".format(PATH3,TODAY)]
        name4 = [r"{}/信用债二级库备选库.xls".format(PATH2),r"{}/XYZEJKBXK{}.csv".format(PATH3,TODAY)]
        name6 = [r"{}/债券禁选池原因{}.xls".format(PATH1,TODAY,TODAY),r"{}/ZQJXCYY{}.csv".format(PATH3,TODAY)]
        if os.path.exists(name6[1]):  # 判断文件是否存在
            os.remove(name6[1])  # 文件每次都要删除，不然会一直变大
        data6 = Dbf5(name6[0],codec = 'gbk')
        data6.to_csv(name6[1])
        name5 = [r"{}/BB-库.xls".format(PATH2),r"{}/BBK{}.csv".format(PATH3,TODAY)]
        self.name5 = name5
        data5 = pd.read_excel(name5[0],converters={u'证券代码':str,u"CODE":str})
        data5.to_csv(name5[1], encoding='gbk')
        names = [name1,name2,name3,name4]
        for name in names:
            self.csv_name_xls.append(name[1])
            data = pd.read_excel(name[0],converters={u'证券代码':str,u"CODE":str})
            data.to_csv(name[1], encoding='gbk')

    def extract_sp_csv1(self):
        self.conn_target.execute_ext("truncate table t_tmp_bsc_pooldata_dbf")
        TARGET_ORM_NAME = TTmpBscPooldataDbf
        df = pd.read_csv(r"{}/HYSJ{}.csv".format(PATH3, TODAY), low_memory=False, encoding='gbk',converters={u"证券代码":str,u"CODE":str})  # 读取的行业数据表，映射关系不一致，单独处理
        df = df.fillna('')
        insert_data = []
        for index, row in df.iterrows():
            target = TARGET_ORM_NAME()
            target.code = row['证券代码']
            target.type1 = row['一级维度编号']
            target.name1 = row['一级维度名称']
            target.market = row['交易市场']
            target.filename = 'HYSJ{}.csv'.format(TODAY)
            insert_data.append(target)
        logger.info('增加{}条'.format(len(insert_data)))
        self.conn_target._add_all(insert_data)
        #年金维度池有特殊字符
        df4 = DBF(self.name4[0], encoding='gbk',
                  char_decode_errors='ignore') #有特殊字符单独处理
        insert_data = []
        for row in df4:
            target = TARGET_ORM_NAME()  # 对象必须每次都创建一个，不然只会增加一个对象。
            for key in TARGET_ORM_NAME.__mapper__.tables[0].columns._data:
                if key != 'filename':
                    setattr(target, key, row[key.upper()])
            target.filename = self.name4[1].split('/')[-1]
            insert_data.append(target)
        logger.info('增加lel{}条'.format(len(insert_data)))
        self.conn_target._add_all(insert_data)
        self.conn_target.save()

    def extract_csv1(self):
        TARGET_ORM_NAME = TTmpBscPooldataDbf
        list_df = []
        for i in self.csv_name:
            df = pd.read_csv(i,low_memory=False, encoding='gbk',converters={u'CODE':str,u"证券代码":str})
            list_df.append(df)
        number = 0
        for df in list_df:
            df = df.fillna('')
            insert_data = []
            for index, row in df.iterrows():
                target = TARGET_ORM_NAME()  
                for key in TARGET_ORM_NAME.__mapper__.tables[0].columns._data:
                    if key != 'filename':
                        setattr(target, key, getattr(row, key.upper()))
                target.filename = self.csv_name[number].split('/')[-1]
                insert_data.append(target)  
            number += 1
            logger.info('增加{}条'.format(len(insert_data)))
            self.conn_target._add_all(insert_data)
            self.conn_target.save()

    def extract_csv2(self):
        #债券禁选池原因
        self.conn_target.execute_ext("truncate table t_tmp_bsc_pooldata_reason")
        TARGET_ORM_NAME = TTmpBscPooldataReason
        df = pd.read_csv(r"{}/ZQJXCYY{}.csv".format(PATH3,TODAY),low_memory=False,encoding='gbk',converters={u'CHID':str,u"证券代码":str,u"CODE":str})
        df = df.fillna('')
        insert_data = []
        for index, row in df.iterrows():
            target = TARGET_ORM_NAME()  
            target.zqdm = row['CHID']
            target.type1 = row['WDID']
            target.name1 = row['WDNA']
            target.scdm = row['CHMKT']
            target.indate = row['indate']
            target.reason_type = ''
            target.reason_typecode = row['typecode']
            target.sname = row['sname']
            target.remark = row['REMARK']
            target.filename = 'ZQJXCYY{}.csv'.format(TODAY)
            insert_data.append(target)  
        logger.info('增加{}条'.format(len(insert_data)))
        self.conn_target._add_all(insert_data)
        self.conn_target.save()

    def extract_csv3(self):
        #PAR_PISTOCK_INFO
        TARGET_ORM_NAME = TTmpBscPooldataReason
        data = DBF(r"{}/PAR_PISTOCK_INFO{}.xls".format(PATH1,TODAY),encoding='gbk',char_decode_errors='ignore')
        insert_data = []
        for row in data:
            target = TARGET_ORM_NAME()
            target.zqdm = row['ZQDM']
            target.scdm = row['SCDM']
            target.indate = row['INDATE']
            target.reason_type = row['TYPE']
            target.reason_typecode = row['TYPECODE']
            target.sname = row['ZQMC']
            target.remark = row['remark']
            target.filename = 'PAR_PISTOCK_INFO{}.csv'.format(TODAY)
            insert_data.append(target)
        logger.info('增加{}条了'.format(len(insert_data)))
        self.conn_target._add_all(insert_data)
        self.conn_target.save()
   

    def extract_xls(self):
        #BB库映射关系不一致，单独处理
        self.conn_target.execute_ext("truncate table t_tmp_bsc_pooldata_xls")
        TARGET_ORM_NAME = TTmpBscPooldataXl
        df = pd.read_csv(self.name5[1], low_memory=False,encoding='gbk',converters={u'证券代码':str,u"CODE":str})     #单独处理的表
        df = df.fillna('')
        insert_data = []
        for index, row in df.iterrows():
            target = TARGET_ORM_NAME()  
            target.filename = self.name5[1].split('/')[-1]
            target.name1 = "BB-库"
            target.market = row['市场名称']
            target.code = row['证券代码']
            insert_data.append(target)
        logger.info('增加le{}条'.format(len(insert_data)))
        self.conn_target.add_all(insert_data)
        self.conn_target.save()
        list_df = []
        for i in self.csv_name_xls:
            df = pd.read_csv(i, low_memory=False, encoding='gbk',converters={u'CODE':str,u"证券代码":str})
            list_df.append(df)
        number = 0
        for df in list_df:
            df = df.fillna('')
            insert_data = []
            i = 0
            for index, row in df.iterrows():
                target = TARGET_ORM_NAME()  
                target.name1 = row['维度名称']
                target.market = row['交易市场']
                target.code = row['证券代码']
                target.weight = row['权重']
                target.cp_gp = row['参考股本']
                target.memo = ''
                target.filename = self.csv_name_xls[number].split('/')[-1]
                insert_data.append(target)  
            number += 1
            logger.debug('增加{}条'.format(len(insert_data)))
            self.conn_target.add_all(insert_data)
            self.conn_target.save()

    def call_pro(self):
        logger.info('开始执行存储过程')
        conn = cx_Oracle.connect('{}/{}@{}/{}'.format(MD_SERVER_USER,MD_SERVER_PASS,MD_SERVER_ADDRESS,MD_SERVICE_NAME))
        cursor = conn.cursor()
        cursor.callproc('p_update_t_bsc_pooldata_dbf')
        if TODAY == time.strftime('%Y%m%d', time.localtime(time.time())):
            cursor.callproc("PKG_POOL_IMPORT.SP_POOL_IMPORT_MOD_FTP",[0])
        else:
            cursor.callproc("PKG_POOL_IMPORT.SP_POOL_IMPORT_MOD_FTP",[1])
        cursor.callproc('PKG_POOL_IMPORT.SP_POOL_IMPORT_MOD_O32')
        cursor.close()
        conn.close()
        logger.info('存储过程执行完成')

    def run(self):
        time1 = time.time()
        self.xls2csv()
        self.dbf2csv()
        self.extract_sp_csv1()
        self.extract_csv1()
        self.extract_csv2()
        self.extract_csv3()
        self.extract_xls()
        self.call_pro()
               
regiest_task("ExtractPool", ExtractPool)
