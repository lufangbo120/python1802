# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscIndustryTk(Base):
    __tablename__ = 't_bsc_industry_tk'

    l_trade_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_industryname = Column(VARCHAR(255))
    vc_industrycode = Column(VARCHAR(255), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_trade_date)+str(self.vc_industrycode)+'$*'+str(self.vc_md5)