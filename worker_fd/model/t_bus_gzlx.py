# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBusGzlx(Base):
    __tablename__ = 't_bus_gzlx'

    gzdm = Column(VARCHAR(6), primary_key=True, nullable=False)
    jxrq = Column(VARCHAR(8), primary_key=True, nullable=False)
    yjlx = Column(VARCHAR(50))
    lxts = Column(NUMBER(6, 0, False))
    pmll = Column(VARCHAR(50))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.jxrq)+str(self.gzdm)+'$*'+str(self.vc_md5)