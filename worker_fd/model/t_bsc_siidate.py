# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscSiidate(Base):
    __tablename__ = 't_bsc_siidate'

    vc_company_code = Column(VARCHAR(16), nullable=False)
    l_sibaseinfoid = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_datetype = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_isinterval = Column(VARCHAR(50), nullable=False)
    l_begin_date = Column(VARCHAR(50), nullable=False)
    l_end_date = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_datetype)+str(self.l_sibaseinfoid)+'$*'+str(self.vc_md5)