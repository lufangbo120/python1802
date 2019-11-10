# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscAiSinkingsubject(Base):
    __tablename__ = 't_bsc_ai_sinkingsubject'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_plancode = Column(VARCHAR(100), primary_key=True, nullable=False)
    vc_companycode = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_subjectname = Column(VARCHAR(200))
    vc_innerindustrycodename = Column(VARCHAR(300))
    vc_areaname = Column(VARCHAR(200))
    l_financialplatform = Column(VARCHAR(50))
    l_platformclass = Column(VARCHAR(50))
    vc_parentinstitutionname = Column(VARCHAR(300))
    vc_parentinstitutioncode = Column(VARCHAR(16))
    vc_funduses = Column(VARCHAR(4000))
    vc_repaysource = Column(VARCHAR(4000))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_companycode)+str(self.vc_plancode)+str(self.l_objid)+'$*'+str(self.vc_md5)