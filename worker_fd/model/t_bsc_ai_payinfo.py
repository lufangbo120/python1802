# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscAiPayinfo(Base):
    __tablename__ = 't_bsc_ai_payinfo'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_ordercode = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_ordername = Column(VARCHAR(100))
    d_startdate = Column(DateTime)
    d_enddate = Column(DateTime)
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_ordercode)+str(self.l_objid)+'$*'+str(self.vc_md5)