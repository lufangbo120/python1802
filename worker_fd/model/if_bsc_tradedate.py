# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscTradedate(Base):
    __tablename__ = 'if_bsc_tradedate'

    l_market = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_market'+'$*'+ 'l_date'