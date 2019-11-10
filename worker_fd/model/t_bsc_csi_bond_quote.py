# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscCsiBondQuote(Base):
    __tablename__ = 't_bsc_csi_bond_quote'

    l_trade_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16))
    l_market = Column(VARCHAR(50))
    en_calculation_price = Column(VARCHAR(50))
    en_maturity_yield = Column(VARCHAR(50))
    en_modified_duration = Column(VARCHAR(50))
    en_convexity = Column(VARCHAR(50))
    en_clean_price = Column(VARCHAR(50))
    en_accrued_interest = Column(VARCHAR(50))
    en_reserve = Column(VARCHAR(50))
    vc_memo = Column(VARCHAR(1024))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_trade_date)+str(self.vc_scode)+'$*'+str(self.vc_md5)