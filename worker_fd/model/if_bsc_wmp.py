# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscWmp(Base):
    __tablename__ = 'if_bsc_wmp'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    l_market = Column(VARCHAR(50))
    vc_wmp_code = Column(VARCHAR(16))
    l_wmp_type = Column(VARCHAR(50))
    l_wmp_category = Column(VARCHAR(50))
    l_wmp_investment = Column(VARCHAR(50))
    vc_company_code = Column(VARCHAR(16))
    l_collect_bdate = Column(NUMBER(8, 0, False))
    l_collect_edate = Column(NUMBER(8, 0, False))
    l_payment_date = Column(VARCHAR(50))
    l_begin_date = Column(VARCHAR(50))
    l_end_date = Column(VARCHAR(50))
    l_interestpay_type = Column(VARCHAR(50))
    c_day_type = Column(CHAR(1))
    en_face_value = Column(VARCHAR(50))
    l_currency = Column(VARCHAR(50))
    en_issue_scale = Column(VARCHAR(50))
    l_interest_type = Column(VARCHAR(50))
    en_expect_yield = Column(VARCHAR(50))
    c_advance_flag = Column(CHAR(1))
    vc_data_source = Column(VARCHAR(32))
    d_updatetime = Column(DateTime)
    vc_md_business_model = Column(VARCHAR(1024))
    vc_remark = Column(VARCHAR(64))
    c_evaluation_type = Column(CHAR(1))
    vc_risk_type = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_scode'