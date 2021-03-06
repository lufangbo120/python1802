# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscAiProduct(Base):
    __tablename__ = 'if_bsc_ai_product'

    l_objid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_validtag = Column(VARCHAR(50))
    vc_planname = Column(VARCHAR(200))
    vc_plancode = Column(VARCHAR(100))
    vc_periodnam = Column(VARCHAR(100))
    vc_periodcod = Column(VARCHAR(50))
    vc_ordername = Column(VARCHAR(100))
    vc_ordercode = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_objid'+'$*'+ 'vc_ordercode'