# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscSecuritycomp(Base):
    __tablename__ = 't_bsc_securitycomp'

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
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_publish_date)+str(self.vc_scode)+str(self.l_relation_market)+str(self.vc_relation_code)+str(self.vc_relation_type)+'$*'+str(self.vc_md5)