# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscSecuritycomp(Base):
    __tablename__ = 'if_bsc_securitycomp'

    l_publish_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_stock_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_relation_type = Column(VARCHAR(32), primary_key=True, nullable=False)
    vc_relation_code = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_relation_market = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50))
    l_end_date = Column(VARCHAR(50))
    c_enable = Column(CHAR(1), nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_publish_date'+'$*'+ 'vc_scode'+'$*'+ 'l_relation_market'+'$*'+ 'vc_relation_code'+'$*'+ 'vc_relation_type'