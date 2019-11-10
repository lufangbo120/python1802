# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MdBscSecuritycomp(Base):
    __tablename__ = 'md_bsc_securitycomp'

    l_publish_date = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_stock_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(NUMBER(scale=0, asdecimal=False), nullable=False)
    vc_relation_type = Column(VARCHAR(32), primary_key=True, nullable=False)
    vc_relation_code = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_relation_market = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    l_begin_date = Column(NUMBER(scale=0, asdecimal=False))
    l_end_date = Column(NUMBER(scale=0, asdecimal=False))
    c_enable = Column(CHAR(1), nullable=False)
    d_updatetime = Column(DateTime, nullable=False)

    def __str__(self):
        return str(self.l_publish_date)+str(self.vc_scode)+str(self.vc_relation_type)+str(self.vc_relation_code)+str(self.l_relation_market)+'$*'+str(self.vc_stock_code)+str(self.l_market)+str(self.l_begin_date)+str(self.l_end_date)+str(self.c_enable)+str(self.d_updatetime)
