# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscPsopreferstock(Base):
    __tablename__ = 'if_bsc_psopreferstock'

    vc_scode = Column(VARCHAR(16), primary_key=True)
    vc_code = Column(VARCHAR(16))
    vc_sname = Column(VARCHAR(128))
    c_is_list = Column(CHAR(1))
    l_market = Column(VARCHAR(50))
    vc_kind = Column(VARCHAR(8))
    l_listdate = Column(VARCHAR(50))
    l_delistdate = Column(VARCHAR(50))
    vc_valuecur = Column(VARCHAR(3))
    en_nst_volume = Column(VARCHAR(50))
    en_nst_scale = Column(VARCHAR(50))
    en_couponrate = Column(VARCHAR(50))
    l_begin_date = Column(VARCHAR(50))
    l_couponrate_adjust = Column(VARCHAR(50))
    l_adjust_unit = Column(VARCHAR(50))
    vc_adjust_desc = Column(VARCHAR(1024))
    vc_repricing_date = Column(VARCHAR(128))
    en_premium = Column(VARCHAR(50))
    l_day_type = Column(VARCHAR(50))
    l_day_mode = Column(VARCHAR(50))
    l_interestpay_times = Column(VARCHAR(50))
    vc_yearpay_date = Column(VARCHAR(128))
    l_nextpay_date = Column(VARCHAR(50))
    c_is_accumulate = Column(CHAR(1))
    c_is_merge = Column(CHAR(1))
    c_is_switch = Column(CHAR(1))
    cl_transfershare_memo = Column(Text)
    en_current_price = Column(VARCHAR(50))
    c_is_call = Column(CHAR(1))
    cl_call_desc = Column(Text)
    c_is_putclause = Column(CHAR(1))
    cl_putclause_desc = Column(Text)
    l_repaymode = Column(VARCHAR(50))
    vc_chgsecode = Column(VARCHAR(36))
    vc_chgsymbol = Column(VARCHAR(36))
    c_as_bond_or_equity = Column(CHAR(1), server_default=text("'3'"))
    vc_eventcode = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_scode'