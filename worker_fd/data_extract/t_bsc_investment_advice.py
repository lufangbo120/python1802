import platform

import cx_Oracle
import os
import pandas as pd
import time

from TopSpeedData_Worker.connection.oracle import connect_target
from model.t_bsc_investment_advice import TBscInvestmentAdvice
from model.t_tmp_bsc_investment_advice import TTmpBscInvestmentAdvice
from settings import MD_SERVER_USER, MD_SERVER_PASS, MD_SERVER_ADDRESS, MD_SERVICE_NAME, logger
from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase, regiest_task
from validation.validation import TValidationObject


class ExtractInvestmentAdvice(TkTaskBase):

    parameterkeys = ['taskid','rundate']

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        #读取参数
        self.conn_target = connect_target()
        self.rundate = self.get_param('rundate')
        self.taskid = self.get_param('taskid')
        rundate = time.strptime(str(self.rundate), "%Y%m%d")
        rundate = time.strftime("%Y.%m.%d",rundate)
        self.ValidationObject = TValidationObject(self.taskid)
        #读取文件     #对应的日期不存在如何处理？
        sysstr = platform.system()
        if sysstr == "Linux":
            self.path = r"/home/tkamc/develop/file/信用债一级发行{}.xlsx".format(rundate)
        else:
            self.path = r"C:\Users\w_lufb\Desktop\信用债\信用债一级发行{}.xlsx".format(rundate)
        self.df1 = pd.read_excel(self.path ,sheet_name='银行间中短期票据投资建议表',skiprows=1)
        self.df2 = pd.read_excel(self.path ,sheet_name='公司债、企业债及其他公开簿记建档发行债券投资建议表',skiprows=1)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self,value):
        if not os.path.exists(value):
            raise Exception("{}文件不存在".format(value))
        self._path = value


    def validate(self, value_list):
        self.ValidationObject.execute(value_list)

    def call_pro(self):

        #删除数据不能按发行日删除，因为当天导入的数据不一定都是当天发行的数据，可以按照导入日期删除。
        self.conn_target.execute_ext("delete from t_bsc_investment_advice where vc_sname in (select vc_sname from t_tmp_bsc_investment_advice) and l_date = {}".format(self.rundate))
        self.conn_target.save()
        conn = cx_Oracle.connect('{}/{}@{}/{}'.format(MD_SERVER_USER,MD_SERVER_PASS,MD_SERVER_ADDRESS,MD_SERVICE_NAME))
        cursor = conn.cursor()
        cursor.callproc('p_update_investment_advice')#存储过程把临时表中数据和证券主表关联后从结果集中取数，vc_code有正式代码取正式的，没有就取临时代码。
        cursor.close()
        conn.close()
        logger.info('存储过程执行完成')
        data = self.conn_target.query(TBscInvestmentAdvice).filter_by(l_date = '{}'.format(self.rundate)).all() #数据读取出来进行校验
        self.validate(data)

    def get_value(self,obj,key): #判断属性是否存在，不存在就赋值为空值。
        if hasattr(obj,key):
            return obj[key]

    def extract_company(self):
        self.conn_target.execute_ext("truncate table t_tmp_bsc_investment_advice")
        df2 = self.df2.fillna('')    #公司债数据
        insert_data = []
        for index, row in df2.iterrows():
            target = TTmpBscInvestmentAdvice()  # 把数据插入临时表
            target.vc_sname = self.get_value(row,'债券简称')
            target.l_issue_date = str(self.get_value(row,'发行日')).split(' ')[0].replace('-','')  #把date类型转换成数字
            target.vc_issuer_name = self.get_value(row,'发行人')
            target.vc_guarantor = self.get_value(row,'担保人')
            target.en_issue_amount = str(self.get_value(row,'规模'))
            target.vc_duration = str(self.get_value(row,'期限'))  #得到的是浮点类型的数，转换成字符串
            target.vc_uwrtname = self.get_value(row,'主承')
            target.vc_creditrate = self.get_value(row,'外部评级')
            target.vc_ratecomname = self.get_value(row,'评级机构')
            target.vc_rate_operator = self.get_value(row,'评级人')
            target.vc_industry_name = self.get_value(row,'行业')
            target.vc_interest_interval = self.get_value(row,'利率区间')
            target.vc_market_rate = self.get_value(row,'市场利率')
            target.vc_investment_advice = self.get_value(row,'投资建议')
            target.vc_referral = self.get_value(row,'推荐人')
            target.vc_bond_type = self.get_value(row, '券种')
            if '(' in  self.get_value(row, '上市'):
                target.vc_market = self.get_value(row, '上市').split('(')[0]
                if len(self.get_value(row, '上市').split('(')) != 1:
                    target.b_pledged = self.get_value(row, '上市').split('(')[1].replace(')','')
            if '（' in  self.get_value(row, '上市'):
                target.vc_market = self.get_value(row, '上市').split('（')[0]
                if len(self.get_value(row, '上市').split('（')) != 1:
                    target.b_pledged = self.get_value(row, '上市').split('（')[1].replace('）','')
            if '(' not in  self.get_value(row, '上市') and '（' not in  self.get_value(row, '上市'):
                target.vc_market = self.get_value(row, '上市')
            target.vc_fundamental = self.get_value(row, '基本面概述')
            sg = self.get_value(row, '申购时间').split('-')
            target.d_bid_begintime = sg[0]
            target.d_bid_endtime = sg[-1]
            if self.get_value(row,'底线价格') == '-':
                target.vc_floor_price = ''
            else:
                target.vc_floor_price = self.get_value(row,'底线价格')
            if self.get_value(row,'备选库') == '√':
                target.b_in_bondpool = '是'
            else:
                target.b_in_bondpool = '否'
            if '初评' in self.get_value(row, '内部评级'):
                target.vc_inner_creditrate = self.get_value(row, '内部评级').replace('初评', '')
                target.vc_primary_rating = '是'
            else:
                target.vc_inner_creditrate = self.get_value(row, '内部评级')
                target.vc_primary_rating = '否'
            if self.get_value(row,'是否假日') == '√':
                target.b_holiday = '是'
            else:
                target.b_holiday = '否'
            target.l_date = int(self.rundate)
            insert_data.append(target)
        self.conn_target.add_all(insert_data)
        self.conn_target.save()

    def extract_bank(self):
        df1 = self.df1.fillna('')
        insert_data = []
        flag = None
        for index, row in df1.iterrows():
            if  hasattr(row,'发行人外评'):
                key1 = '发行人外评'
                key2 =  '发行人内评'
            if  hasattr(row,'外评'):
                key1 = '外评'
                key2 = '内评'
            if  hasattr(row,'外部评级'):
                key1 = '外部评级'
                key2 = '内部评级'
            target = TTmpBscInvestmentAdvice()  # 把数据插入临时表
            target.vc_sname = self.get_value(row,'债券简称')
            target.l_issue_date = str(self.get_value(row,'发行日')).split(' ')[0].replace('-', '')  # 把date类型转换成数字
            target.vc_issuer_name = self.get_value(row,'发行人')
            target.vc_guarantor = self.get_value(row,'担保人')
            target.en_issue_amount = str(self.get_value(row,'规模'))
            target.vc_duration = str(self.get_value(row,'期限'))  # 得到的是浮点类型的数，转换成字符串
            target.vc_uwrtname = self.get_value(row,'主承')
            target.vc_creditrate = self.get_value(row,key1)
            target.vc_ratecomname = self.get_value(row,'评级机构')
            target.vc_market = '银行间'
            target.vc_rate_operator = self.get_value(row,'评级人')
            target.vc_industry_name = self.get_value(row,'行业')
            target.vc_interest_interval = self.get_value(row,'利率区间')
            target.vc_market_rate = self.get_value(row,'市场利率')
            target.vc_investment_advice = self.get_value(row, '投资建议')
            target.vc_referral = self.get_value(row, '推荐人')
            target.vc_star_level = self.get_value(row,'推荐星级')
            if self.get_value(row, '类别') != '':
                target.vc_advice_type = self.get_value(row, '类别')
                flag = self.get_value(row, '类别')
            else:
                target.vc_advice_type = flag
            if '初评' in self.get_value(row, key2):
                target.vc_inner_creditrate = self.get_value(row, key2).replace('初评', '')
                target.vc_primary_rating = '是'
            else:
                target.vc_inner_creditrate = self.get_value(row, key2)
                target.vc_primary_rating = '否'
            if self.get_value(row,'推荐利率') == '-' or self.get_value(row,'推荐利率') == '/':
                target.vc_advice_rate = ''
            else:
                target.vc_advice_rate = self.get_value(row,'推荐利率')
            if self.get_value(row,'备选库') == '√':
                target.b_in_bondpool = '是'
            else:
                target.b_in_bondpool = '否'
            if self.get_value(row,'假日到期') == '√':
                target.b_holiday = '是'
            else:
                target.b_holiday = '否'
            if self.get_value(row,'底限价格') == '-':
                target.vc_floor_price = ''
            else:
                target.vc_floor_price = self.get_value(row,'底限价格')
            target.l_date = int(self.rundate)
            insert_data.append(target)

        self.conn_target.add_all(insert_data)
        self.conn_target.save()

    def check_sname(self):
        tmp_data = self.conn_target.execute("select vc_sname from t_tmp_bsc_investment_advice group by vc_sname having count(*)>1") #数据读取出来进行校验
        if tmp_data != []:
            logger.info("证券简称为{}的债券重复".format(tmp_data[0][0]))


    def run(self):
        self.extract_company()
        self.extract_bank()
        self.check_sname()
        self.call_pro()
regiest_task("ExtractInvestmentAdvice", ExtractInvestmentAdvice)


