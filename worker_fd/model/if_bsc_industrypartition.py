# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscIndustrypartition(Base):
    __tablename__ = 'if_bsc_industrypartition'

    vc_partmode = Column(NUMBER(20, 0, False), primary_key=True, nullable=False)
    vc_industry = Column(VARCHAR(20))
    vc_industrycode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_industryname = Column(VARCHAR(100))
    vc_findusrty = Column(VARCHAR(40), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime, server_default=text("SYSDATE"))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_partmode'+'$*'+ 'vc_industrycode'+'$*'+ 'vc_findusrty'