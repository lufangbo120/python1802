# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscPoolTk(Base):
    __tablename__ = 't_bsc_pool_tk'

    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_trade_no = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_trade_name = Column(VARCHAR(256))
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16))
    vc_name = Column(VARCHAR(100))
    l_market = Column(VARCHAR(50))
    vc_reason = Column(VARCHAR(1024), primary_key=True, nullable=False)
    vc_memo = Column(VARCHAR(1024))
    l_flag = Column(VARCHAR(50))
    d_entrydate = Column(DateTime)
    vc_entrytime = Column(VARCHAR(16))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_date)+str(self.vc_trade_no)+str(self.vc_reason)+str(self.vc_scode)+'$*'+str(self.vc_md5)