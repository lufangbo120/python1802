# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBdcestimate(Base):
    __tablename__ = 'if_bsc_bdcestimate'

    l_trade_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_sname = Column(VARCHAR(100))
    en_close_price = Column(VARCHAR(50))
    en_convbond_price = Column(VARCHAR(50))
    en_discount_rate = Column(VARCHAR(50))
    en_interest = Column(VARCHAR(50))
    en_convert_price = Column(VARCHAR(50))
    en_convprem = Column(VARCHAR(50))
    en_convprem_rate = Column(VARCHAR(50))
    en_convet_price = Column(VARCHAR(50))
    en_convprem_per = Column(VARCHAR(50))
    en_current_yield = Column(VARCHAR(50))
    en_pure_value = Column(VARCHAR(50))
    en_pure_prem = Column(VARCHAR(50))
    en_pure_premrate = Column(VARCHAR(50))
    en_convpure_price = Column(VARCHAR(50))
    en_mat_yield = Column(VARCHAR(50))
    en_conv_ratio = Column(VARCHAR(50))
    en_net_rate = Column(VARCHAR(50))
    en_latest_price = Column(VARCHAR(50))
    en_arbitrage = Column(VARCHAR(50))
    l_if_deal = Column(CHAR(1))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_trade_date'+'$*'+ 'vc_scode'