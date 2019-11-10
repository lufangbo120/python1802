# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBond(Base):
    __tablename__ = 'if_bsc_bond'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_bond_year = Column(VARCHAR(4))
    vc_company_code = Column(VARCHAR(16), nullable=False)
    vc_issue_entity = Column(VARCHAR(128), nullable=False)
    l_bond_form = Column(VARCHAR(50), nullable=False)
    c_is_collectionbill = Column(CHAR(1))
    l_bond_type = Column(VARCHAR(50), nullable=False)
    l_bond_asset = Column(VARCHAR(50))
    c_is_collectionenterprisedebt = Column(CHAR(1))
    l_other_classification = Column(VARCHAR(50))
    l_bondinterest_type = Column(VARCHAR(50), nullable=False)
    en_couponrate = Column(VARCHAR(50), nullable=False)
    l_intecalc_method = Column(VARCHAR(50), nullable=False)
    l_interest_type = Column(VARCHAR(50), nullable=False)
    l_interestpay_type = Column(VARCHAR(50), nullable=False)
    l_intecalc_rule = Column(VARCHAR(50), nullable=False)
    l_benchmarkrate_type = Column(VARCHAR(50))
    en_benchmarkmargin = Column(VARCHAR(50))
    c_is_guaranty = Column(CHAR(1))
    en_guaranty_rate = Column(VARCHAR(50))
    l_rate_adjustmode = Column(VARCHAR(50))
    l_offer_date = Column(VARCHAR(50), nullable=False)
    l_begin_date = Column(VARCHAR(50), nullable=False)
    l_cease_date = Column(VARCHAR(50))
    l_end_date = Column(VARCHAR(50), nullable=False)
    en_maturity = Column(VARCHAR(50), nullable=False)
    en_par_value = Column(VARCHAR(50), nullable=False)
    en_issue_price = Column(VARCHAR(50), nullable=False)
    en_issue_scale = Column(VARCHAR(50), nullable=False)
    c_is_callbond = Column(CHAR(1))
    l_call_date = Column(VARCHAR(50))
    c_is_putbond = Column(CHAR(1))
    l_put_date = Column(VARCHAR(50))
    c_is_ccbond = Column(CHAR(1))
    c_is_ewbond = Column(CHAR(1))
    c_is_strips = Column(CHAR(1))
    c_is_exchgbond = Column(CHAR(1))
    c_if_guarantee = Column(CHAR(1))
    c_is_govsupport_bond = Column(CHAR(1))
    c_progressive_type = Column(CHAR(1))
    en_progressive_rate = Column(VARCHAR(50))
    vc_credit_rank = Column(VARCHAR(16))
    l_extcredit_enhancemode = Column(VARCHAR(50))
    l_stub_adjustment = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_data_source = Column(VARCHAR(32), nullable=False)
    d_src_updatetime = Column(DateTime, nullable=False)
    l_source_id = Column(NUMBER(18, 0, False), nullable=False)
    c_is_sustainbond = Column(CHAR(1))
    vc_bondgroup_code = Column(VARCHAR(32))
    c_is_perpetual = Column(CHAR(1))
    c_as_bond_or_equity = Column(CHAR(1))
    vc_temp_code = Column(VARCHAR(16))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_scode'