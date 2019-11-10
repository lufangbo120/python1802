# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscBondinterpayment(Base):
    __tablename__ = 't_bsc_bondinterpayments'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_pay_seq = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_paydate_peryear = Column(VARCHAR(8))
    l_paydate_first = Column(VARCHAR(50))
    l_paydate_last = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  '$*'+str(self.vc_md5)