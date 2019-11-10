# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondestimate(Base):
    __tablename__ = 'if_bsc_bondestimate'

    l_data_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_estimate_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_nprice = Column(VARCHAR(50))
    en_fprice = Column(VARCHAR(50))
    en_interest = Column(VARCHAR(50))
    en_years = Column(VARCHAR(50))
    en_yield = Column(VARCHAR(50))
    en_duration = Column(VARCHAR(50))
    en_mduration = Column(VARCHAR(50))
    en_convexity = Column(VARCHAR(50))
    en_diffduration = Column(VARCHAR(50))
    en_diffconvexity = Column(VARCHAR(50))
    en_basispointval = Column(VARCHAR(50))
    en_ratioduration = Column(VARCHAR(50))
    en_ratioconvexity = Column(VARCHAR(50))
    en_residual_capital = Column(VARCHAR(50))
    en_spread = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_estimate_date'+'$*'+ 'vc_scode'+'$*'+ 'l_data_type'