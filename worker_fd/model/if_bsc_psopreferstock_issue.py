# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscPsopreferstockIssue(Base):
    __tablename__ = 'if_bsc_psopreferstock_issue'

    vc_scode = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16))
    l_publishdate = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_updatedate = Column(VARCHAR(50))
    vc_issue_type = Column(VARCHAR(4))
    vc_company_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    l_offer_times = Column(VARCHAR(50))
    vc_issue_mode = Column(VARCHAR(4))
    vc_issuetype_memo = Column(VARCHAR(1024))
    vc_currency = Column(VARCHAR(4))
    en_face_value = Column(VARCHAR(50))
    en_couponrate = Column(VARCHAR(50))
    en_benchmarkmargin = Column(VARCHAR(50))
    vc_baserate_code = Column(VARCHAR(16))
    vc_rate_methods = Column(VARCHAR(2048))
    en_couponrate_max = Column(VARCHAR(50))
    en_couponrate_min = Column(VARCHAR(50))
    l_begin_date = Column(VARCHAR(50))
    en_issue_scale_act = Column(VARCHAR(50))
    en_issue_price = Column(VARCHAR(50))
    en_collect_act = Column(VARCHAR(50))
    en_collect_net_act = Column(VARCHAR(50))
    en_issue_exp_tot = Column(VARCHAR(50))
    en_issue_exp_per = Column(VARCHAR(50))
    l_issue_status = Column(VARCHAR(50))
    c_isvalid = Column(CHAR(1))
    c_ispublic = Column(CHAR(1))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_company_code'+'$*'+ 'l_publishdate'+'$*'+ 'vc_scode'