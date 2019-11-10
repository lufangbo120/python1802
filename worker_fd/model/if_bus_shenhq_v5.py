# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusShenhqV5(Base):
    __tablename__ = 'if_bus_shenhq_v5'

    vc_securityid = Column(VARCHAR(8), primary_key=True, nullable=False)
    vc_securityidsource = Column(VARCHAR(8))
    vc_symbol = Column(VARCHAR(40))
    vc_englishname = Column(VARCHAR(40))
    en_securitytype = Column(NUMBER(8, 0, False))
    en_prevclosepx = Column(VARCHAR(50))
    en_openprice = Column(VARCHAR(50))
    en_closepx = Column(VARCHAR(50))
    en_numtrades = Column(NUMBER(20, 0, False))
    en_totalvolumetrade = Column(VARCHAR(50))
    en_totalvaluetrade = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, server_default=text("sysdate"))
    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_date'+'$*'+ 'vc_securityid'