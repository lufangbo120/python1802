# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscSuspensionstockquote(Base):
    __tablename__ = 't_bsc_suspensionstockquote'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_stock_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_estimate_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_index_code = Column(VARCHAR(16))
    vc_index_name = Column(VARCHAR(100))
    l_trade_date = Column(VARCHAR(50))
    en_suspension_price = Column(VARCHAR(50))
    en_suspension_index = Column(VARCHAR(50))
    en_latest_index = Column(VARCHAR(50))
    en_price = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_estimate_date)+str(self.vc_scode)+'$*'+str(self.vc_md5)