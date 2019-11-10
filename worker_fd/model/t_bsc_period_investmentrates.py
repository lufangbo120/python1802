# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscPeriodInvestmentrate(Base):
    __tablename__ = 't_bsc_period_investmentrates'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_periodcode = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_floattimelimit = Column(VARCHAR(50))
    en_ratebase = Column(VARCHAR(50))
    en_margin = Column(VARCHAR(50))
    en_expectedyieldlimit = Column(VARCHAR(50))
    en_expectedyieldlower = Column(VARCHAR(50))
    vc_userdefinedrate = Column(VARCHAR(4000))
    l_adjusttype = Column(VARCHAR(50))
    en_productrate = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_objid)+str(self.vc_periodcode)+'$*'+str(self.vc_md5)