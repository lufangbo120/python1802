# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusShanghq(Base):
    __tablename__ = 'if_bus_shanghq'

    s1 = Column(VARCHAR(6), primary_key=True, nullable=False)
    s2 = Column(VARCHAR(8))
    s3 = Column(VARCHAR(50))
    s4 = Column(VARCHAR(50))
    s5 = Column(VARCHAR(50))
    s6 = Column(VARCHAR(50))
    s7 = Column(VARCHAR(50))
    s8 = Column(VARCHAR(50))
    s9 = Column(VARCHAR(50))
    s10 = Column(VARCHAR(50))
    s11 = Column(VARCHAR(50))
    s13 = Column(VARCHAR(50))
    s15 = Column(VARCHAR(50))
    s16 = Column(VARCHAR(50))
    s17 = Column(VARCHAR(50))
    s18 = Column(VARCHAR(50))
    s19 = Column(VARCHAR(50))
    s21 = Column(VARCHAR(50))
    s22 = Column(VARCHAR(50))
    s23 = Column(VARCHAR(50))
    s24 = Column(VARCHAR(50))
    s25 = Column(VARCHAR(50))
    s26 = Column(VARCHAR(50))
    s27 = Column(VARCHAR(50))
    s28 = Column(VARCHAR(50))
    s29 = Column(VARCHAR(50))
    s30 = Column(VARCHAR(50))
    s31 = Column(VARCHAR(50))
    s32 = Column(VARCHAR(50))
    s33 = Column(VARCHAR(50))
    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    mdstreamid = Column(VARCHAR(8))
    tradeprice = Column(VARCHAR(50))
    precloseiopv = Column(VARCHAR(50))
    iopv = Column(VARCHAR(50))
    tradingphasecode = Column(VARCHAR(8))
    timestamp = Column(VARCHAR(16))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return   's1'+'$*'+ 'l_date'