# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscPensionproduct(Base):
    __tablename__ = 't_bsc_pensionproduct'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_pf_code = Column(VARCHAR(20))
    l_market = Column(VARCHAR(50))
    vc_company_code = Column(VARCHAR(8))
    vc_classcode1 = Column(VARCHAR(10))
    vc_classcode2 = Column(VARCHAR(10))
    l_begin_date = Column(VARCHAR(50))
    l_end_date = Column(VARCHAR(50))
    en_expect_yield = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    vc_md_business_model = Column(VARCHAR(1024))
    vc_risk_type = Column(VARCHAR(32))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_scode)+'$*'+str(self.vc_md5)