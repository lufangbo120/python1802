# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscFundnav(Base):
    __tablename__ = 'if_bsc_fundnav'

    vc_scode = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_fund_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_nav_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_unet_value = Column(VARCHAR(50))
    en_unet_avalue = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    en_asset_value = Column(VARCHAR(50))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_nav_date'+'$*'+ 'vc_scode'