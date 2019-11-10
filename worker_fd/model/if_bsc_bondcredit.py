# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondcredit(Base):
    __tablename__ = 'if_bsc_bondcredit'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16))
    l_market = Column(VARCHAR(50))
    vc_ratecompany_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    l_rate_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_credit_rank = Column(VARCHAR(16))
    l_credit_anticipate = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    l_declare_date = Column(VARCHAR(50))
    vc_ratestyle = Column(VARCHAR(2))
    vc_changeway = Column(VARCHAR(2))
    vc_cevaluit = Column(VARCHAR(100))
    vc_changereason = Column(VARCHAR(500))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_ratecompany_code'+'$*'+ 'vc_scode'+'$*'+ 'l_end_date'+'$*'+ 'l_begin_date'+'$*'+ 'l_rate_type'