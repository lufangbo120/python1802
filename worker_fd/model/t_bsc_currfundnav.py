# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscCurrfundnav(Base):
    __tablename__ = 't_bsc_currfundnav'

    vc_scode = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_fund_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_publish_date = Column(VARCHAR(50))
    l_begin_date = Column(VARCHAR(50))
    l_trade_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_nav_flag = Column(VARCHAR(3), primary_key=True, nullable=False)
    en_profit = Column(VARCHAR(50))
    l_unit = Column(VARCHAR(50))
    en_aprofit_1w = Column(VARCHAR(50))
    en_yield_7d = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    en_asset_value = Column(VARCHAR(50))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_trade_date)+str(self.vc_scode)+str(self.vc_nav_flag)+'$*'+str(self.vc_md5)