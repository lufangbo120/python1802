from extract_base.t_data_base import TDataBase, CONST_SEPARATOR
from data_extract.t_data_md5 import TDataMD5

from settings import logger
from TopSpeedData_Worker.tkacmbase.taskbase import regiest_task


class TOdsSecuritycomp(TDataMD5):

    def load_source_data(self):
        source_data1 = self.config.conn_source.execute('select * from hs_trade.if_bsc_securitycomp')
        source_data = self.config.conn_target.execute('select * from t_ods_securitycomp')
        source_data.extend(source_data1)
        self.source_data = source_data
        return source_data

    def load_target_data(self):
        '''把源表提取写成sql'''
        self.config.conn_target.execute_ext('delete from  t_ods_securitycomp')
        self.config.conn_target.save()
        data = self.config.conn_source.execute(
            "select  substr(vc_assign_code,1,length(vc_assign_code)-2)||decode(l_market,1,'SH',2,'SZ',3,'YH',4,'MF',5,'ZJ',7,'GT',8,'HK',10,'NE',17,'GG',18,'SG') vc_scode,vc_assign_code,l_market,vc_report_code,d_updatetime from hs_trade.if_bsc_stockinfo t where t.l_date=to_char(sysdate,'yyyymmdd') and  substr(t.vc_report_code,2,1) = 'x' and substr(t.vc_assign_code,2,1) != 'x'")
        data1 = self.config.conn_source.execute(
            "select  substr(vc_assign_code,1,length(vc_assign_code)-2)||decode(l_market,1,'SH',2,'SZ',3,'YH',4,'MF',5,'ZJ',7,'GT',8,'HK',10,'NE',17,'GG',18,'SG') vc_scode,vc_assign_code,l_market,vc_report_code,d_updatetime from hs_trade.if_bsc_stockinfo t where t.l_date=to_char(sysdate,'yyyymmdd') and  substr(t.vc_report_code,2,1) = 'd' and substr(t.vc_assign_code,2,1) != 'd'")
        for i in data:
            self.config.conn_target.execute_ext(
                "insert into t_ods_securitycomp values ('19000101','{0}','{1}','{2}','TK005','{3}','{4}',null,null,'1',to_date('{5}','yyyy-mm-dd hh24:mi:ss'),'','')"
                    .format(i.vc_scode, i.vc_assign_code[:-2], i.l_market,
                            i['vc_report_code'],
                            i.l_market, i.d_updatetime))
        self.config.conn_target.save()
        for i in data1:
            self.config.conn_target.execute_ext(
                "insert into t_ods_securitycomp values ('19000101','{0}','{1}','{2}','TK004','{3}','{4}',null,null,'1',to_date('{5}','yyyy-mm-dd hh24:mi:ss'),'','')"
                    .format(i.vc_scode, i.vc_assign_code[:-2], i.l_market,
                            i['vc_report_code'],
                            i.l_market, i.d_updatetime))
        self.config.conn_target.save()
        target_data = self.config.conn_target.query(self.config.target_orm_name).all()
        self.target_data = target_data
        return target_data

    def delete_save(self):
        '''这张表不删除数据'''
        pass


regiest_task("TOdsSecuritycomp", TOdsSecuritycomp)
