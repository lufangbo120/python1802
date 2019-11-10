# coding: utf-8
from sqlalchemy import Column, TIMESTAMP, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscTl4(Base):
    __tablename__ = 'if_bsc_tl4'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_kind = Column(VARCHAR(20))
    vc_tl4 = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(TIMESTAMP)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_scode'+'$*'+ 'l_end_date'+'$*'+ 'l_begin_date'+'$*'+ 'vc_tl4'