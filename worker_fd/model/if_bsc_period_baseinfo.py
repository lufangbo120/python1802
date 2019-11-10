# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscPeriodBaseinfo(Base):
    __tablename__ = 'if_bsc_period_baseinfo'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_periodcode = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_periodname = Column(VARCHAR(100))
    l_isshowth = Column(VARCHAR(50))
    vc_planstatus = Column(VARCHAR(200))
    vc_abbreviation = Column(VARCHAR(200))
    l_nointerestrates = Column(VARCHAR(50))
    l_ratetype = Column(VARCHAR(50))
    en_beneficiaryfirstrate = Column(VARCHAR(50))
    en_firstrate = Column(VARCHAR(50))
    l_interestpatterns = Column(VARCHAR(50))
    l_interestmode = Column(VARCHAR(50))
    l_ratedecimalway = Column(VARCHAR(50))
    l_ratedecimaldigits = Column(VARCHAR(50))
    d_firstdate = Column(DateTime)
    vc_ratebearingdatetxt = Column(VARCHAR(1000))
    vc_ratebearingdelay = Column(VARCHAR(1000))
    l_interestpaymentday = Column(VARCHAR(50))
    vc_depositoption = Column(VARCHAR(40))
    vc_remarks = Column(VARCHAR(4000))
    en_paydebttype = Column(VARCHAR(50))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return   'vc_periodcode'+'$*'+ 'l_objid'