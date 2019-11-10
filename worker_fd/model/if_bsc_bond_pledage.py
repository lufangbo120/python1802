# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondPledage(Base):
    __tablename__ = 'if_bsc_bond_pledage'

    vc_code = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_name = Column(VARCHAR(200))
    l_mktcode = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_accountid = Column(VARCHAR(8), primary_key=True, nullable=False)
    vc_accountname = Column(VARCHAR(50))
    l_limitid = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_limitidtype = Column(VARCHAR(50))
    vc_inputname = Column(VARCHAR(120))
    l_compliance = Column(VARCHAR(50))
    vc_reason = Column(VARCHAR(200))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_code'+'$*'+ 'vc_accountid'+'$*'+ 'l_mktcode'+'$*'+ 'l_limitid'