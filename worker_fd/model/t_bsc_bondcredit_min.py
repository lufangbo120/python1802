# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscBondcreditMin(Base):
    __tablename__ = 't_bsc_bondcredit_min'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16))
    l_market = Column(VARCHAR(50))
    vc_ratecompany_name = Column(VARCHAR(128))
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    c_credit_rank = Column(CHAR(1))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_scode)+str(self.l_end_date)+str(self.l_begin_date)+'$*'+str(self.vc_md5)