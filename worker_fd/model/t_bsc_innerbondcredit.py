# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscInnerbondcredit(Base):
    __tablename__ = 't_bsc_innerbondcredit'

    vc_scode = Column(VARCHAR(36), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(32))
    l_market = Column(VARCHAR(50))
    l_rate_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_credit_rank = Column(VARCHAR(16))
    l_credit_anticipate = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  '$*'+str(self.vc_md5)