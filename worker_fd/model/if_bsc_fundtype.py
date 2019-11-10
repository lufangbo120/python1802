# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscFundtype(Base):
    __tablename__ = 'if_bsc_fundtype'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_fund_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), nullable=False)
    l_data_kind = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_type_no = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_type_no'+'$*'+ 'vc_scode'+'$*'+ 'l_data_kind'+'$*'+ 'l_begin_date'