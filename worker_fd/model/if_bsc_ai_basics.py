# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscAiBasic(Base):
    __tablename__ = 'if_bsc_ai_basics'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_planname = Column(VARCHAR(500))
    vc_plancode = Column(VARCHAR(100), primary_key=True, nullable=False)
    vc_producttype = Column(VARCHAR(50))
    vc_pmrecordcode = Column(VARCHAR(200))
    en_offeringsize = Column(VARCHAR(50))
    vc_partakeway = Column(VARCHAR(50))
    l_whetherproject = Column(VARCHAR(50))
    vc_addcredittype = Column(VARCHAR(100))
    vc_addcreditremarks = Column(VARCHAR(4000))
    en_guaranteedbreakeven = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_objid'+'$*'+ 'vc_plancode'