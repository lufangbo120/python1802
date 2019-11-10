# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscZzdbondestimate(Base):
    __tablename__ = 't_bsc_zzdbondestimate'

    zqjc = Column(VARCHAR(100))
    zqdm = Column(VARCHAR(20), primary_key=True, nullable=False)
    gzrq = Column(VARCHAR(50), primary_key=True, nullable=False)
    csjc = Column(VARCHAR(64), primary_key=True, nullable=False)
    sjdcq = Column(VARCHAR(50))
    gjqj = Column(VARCHAR(50))
    yjlx = Column(VARCHAR(50))
    gjjj = Column(VARCHAR(50))
    gjsyl = Column(VARCHAR(50))
    evlxzjq = Column(VARCHAR(50))
    evltx = Column(VARCHAR(50))
    evljdjz = Column(VARCHAR(50))
    evllcjq = Column(VARCHAR(50))
    evllctx = Column(VARCHAR(50))
    zsqj = Column(VARCHAR(50))
    zsjj = Column(VARCHAR(50))
    zssyl = Column(VARCHAR(50))
    realxzjq = Column(VARCHAR(50))
    realtx = Column(VARCHAR(50))
    realjdjz = Column(VARCHAR(50))
    reallcjq = Column(VARCHAR(50))
    reallctx = Column(VARCHAR(50))
    kxd = Column(VARCHAR(32), primary_key=True, nullable=False)
    evllljq = Column(VARCHAR(50))
    evllltx = Column(VARCHAR(50))
    reallljq = Column(VARCHAR(50))
    reallltx = Column(VARCHAR(50))
    rzgjqj = Column(VARCHAR(50))
    rzyjlx = Column(VARCHAR(50))
    sybj = Column(VARCHAR(50))
    vc_listgmktbd = Column(VARCHAR(32))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.kxd)+str(self.csjc)+str(self.gzrq)+str(self.zqdm)+'$*'+str(self.vc_md5)