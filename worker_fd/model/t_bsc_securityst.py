# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscSecurityst(Base):
    __tablename__ = 't_bsc_securityst'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_stock_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(NUMBER(scale=0, asdecimal=False), nullable=False)
    l_st_type = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    l_st_date = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    l_endst_date = Column(NUMBER(scale=0, asdecimal=False))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    l_delete = Column(NUMBER(scale=0, asdecimal=False), server_default=text("0"))

    def __str__(self):
        return  str(self.l_st_type)+str(self.vc_scode)+str(self.l_st_date)+'$*'+str(self.vc_md5)