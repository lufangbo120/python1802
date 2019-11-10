# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Tstockinfo(Base):
    __tablename__ = 'tstockinfo'

    l_date = Column(NUMBER(8, 0, False), primary_key=True, nullable=False)
    vc_inter_code = Column(VARCHAR(8), primary_key=True, nullable=False)
    l_market = Column(NUMBER(asdecimal=False))
    vc_report_code = Column(VARCHAR(20))
    vc_stock_name = Column(VARCHAR(100))
    c_stock_type = Column(VARCHAR(2))
    c_asset_type = Column(CHAR(1))
    vc_asset_relative_code = Column(VARCHAR(8))
    vc_currency = Column(VARCHAR(3))
    vc_mixed_type = Column(VARCHAR(100))
    vc_international_code = Column(VARCHAR(32))
    vc_busin_classes = Column(VARCHAR(512))
    c_default_price = Column(CHAR(1))
    en_reference_price = Column(NUMBER(16, 8, True))
    l_publish_date = Column(NUMBER(8, 0, False))
    l_turnover_date = Column(NUMBER(8, 0, False))
    l_total_lock_day = Column(NUMBER(scale=0, asdecimal=False))
    l_left_lock_days = Column(NUMBER(scale=0, asdecimal=False))
    vc_assign_code = Column(VARCHAR(20))

    def __str__(self):
        return   'l_date'+'$*'+ 'vc_inter_code'