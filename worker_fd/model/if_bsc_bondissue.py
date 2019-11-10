# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondissue(Base):
    __tablename__ = 'if_bsc_bondissue'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_issue_type = Column(VARCHAR(3), primary_key=True, nullable=False)
    l_issue_cnt = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_issue_volume = Column(VARCHAR(50))
    en_face_value = Column(VARCHAR(50))
    c_is_tender = Column(CHAR(1))
    l_publicoffer_type = Column(VARCHAR(50))
    en_issue_price = Column(VARCHAR(50))
    l_list_date = Column(VARCHAR(50))
    l_issue_begin_date = Column(DateTime)
    l_issue_end_date = Column(DateTime)
    l_bid_date = Column(DateTime)
    l_pay_date = Column(DateTime)
    l_declare_date = Column(DateTime)
    en_issue_amount_plan = Column(VARCHAR(50))
    en_issue_amount_act = Column(VARCHAR(50))
    l_underwrite_manner = Column(VARCHAR(2))
    vc_bid_target = Column(VARCHAR(50))
    l_bid_type = Column(VARCHAR(2))
    en_bid_limit_upper = Column(VARCHAR(50))
    en_bid_limit_lower = Column(VARCHAR(50))
    en_issue_rate = Column(VARCHAR(50))
    vc_code_online = Column(VARCHAR(20))
    vc_issue_result = Column(VARCHAR(2000))
    en_purchase_lim_low = Column(VARCHAR(50))
    en_add_purchase_unit = Column(VARCHAR(50))
    l_pre_market = Column(VARCHAR(50))
    en_issue_offline_amount = Column(VARCHAR(50))
    en_agreement_amount = Column(VARCHAR(50))
    en_reference_rate = Column(VARCHAR(50))
    en_fee_rate = Column(VARCHAR(50))
    en_issue_fee = Column(VARCHAR(50))
    en_issue_object = Column(VARCHAR(2000))
    en_raise_amount = Column(VARCHAR(50))
    en_sale_quantity = Column(VARCHAR(50))
    en_sale_amount = Column(VARCHAR(50))
    en_sale_fee = Column(VARCHAR(50))
    en_exclusive_quantity = Column(VARCHAR(50))
    en_avg_period = Column(VARCHAR(50))
    d_plan_enddate = Column(DateTime)
    en_online_issue_amount = Column(VARCHAR(50))
    d_law_enddate = Column(DateTime)
    l_bondiriid = Column(VARCHAR(50))
    vc_bid_time = Column(VARCHAR(2000))
    d_bid_enddate = Column(DateTime)
    d_updatetime = Column(DateTime, nullable=False)
    vc_update_operater = Column(VARCHAR(20))
    vc_source = Column(VARCHAR(20))

    def __str__(self):
        return   'l_issue_cnt'+'$*'+ 'vc_issue_type'+'$*'+ 'vc_scode'