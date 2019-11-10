# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscHkequityquote(Base):
    __tablename__ = 'if_bsc_hkequityquote'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_stock_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_trade_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_last_price = Column(VARCHAR(50))
    en_open_price = Column(VARCHAR(50))
    en_high_price = Column(VARCHAR(50))
    en_low_price = Column(VARCHAR(50))
    en_close_price = Column(VARCHAR(50))
    en_amount = Column(VARCHAR(50))
    en_volume = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_trade_date'+'$*'+ 'vc_scode'