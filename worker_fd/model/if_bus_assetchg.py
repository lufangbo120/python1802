# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusAssetchg(Base):
    __tablename__ = 'if_bus_assetchg'

    c_business_type = Column(CHAR(2), primary_key=True, nullable=False)
    c_fund_code = Column(CHAR(6), primary_key=True, nullable=False)
    c_trade_ask_date = Column(CHAR(8))
    en_turnover_share = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_turnover_money = Column(VARCHAR(50))
    en_total_cost = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_trade_fee = Column(VARCHAR(50))
    en_transfer_fee = Column(VARCHAR(50))
    en_stamp_duty = Column(VARCHAR(50))
    en_post_charge = Column(VARCHAR(50))
    en_other_fee = Column(VARCHAR(50))
    en_fund_assets_fee = Column(VARCHAR(50))
    c_settlement_date = Column(CHAR(8))
    c_processing_date = Column(CHAR(8))
    en_unit_bonus = Column(VARCHAR(50))
    c_sales_agency = Column(CHAR(3))
    d_updatetime = Column(DateTime)
    vc_data_source = Column(VARCHAR(4))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'c_business_type'+'$*'+ 'en_total_cost'+'$*'+ 'c_fund_code'+'$*'+ 'en_turnover_share'