# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBusShengb(Base):
    __tablename__ = 't_bus_shengb'

    gblb = Column(VARCHAR(8), primary_key=True)
    gbdm1 = Column(VARCHAR(16))
    gbdm2 = Column(VARCHAR(32))
    gbsl = Column(NUMBER(17, 2, True))
    gbrq1 = Column(VARCHAR(8))
    gbrq2 = Column(VARCHAR(8))
    gbbl = Column(NUMBER(19, 13, True))
    gbje1 = Column(NUMBER(18, 3, True))
    gbje2 = Column(NUMBER(18, 3, True))
    gbzd = Column(VARCHAR(100))
    gbrq = Column(VARCHAR(8))
    gbdm3 = Column(VARCHAR(32))
    gbbz1 = Column(CHAR(1))
    gbbz2 = Column(CHAR(1))
    gbbzsm = Column(VARCHAR(100))
    gbsl2 = Column(NUMBER(17, 2, True))
    gbbl2 = Column(NUMBER(19, 13, True))
    gbrq3 = Column(VARCHAR(8))
    gbrq4 = Column(VARCHAR(8))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.gblb)+'$*'+str(self.vc_md5)