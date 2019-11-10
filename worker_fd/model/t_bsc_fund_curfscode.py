# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscFundCurfscode(Base):
    __tablename__ = 't_bsc_fund_curfscode'

    l_curfscodeid = Column(VARCHAR(50))
    l_declaredate = Column(VARCHAR(50))
    vc_symbol = Column(VARCHAR(6), primary_key=True, nullable=False)
    vc_sname = Column(VARCHAR(100))
    vc_symbol_comp = Column(VARCHAR(6), primary_key=True, nullable=False)
    vc_sname_comp = Column(VARCHAR(100))
    l_begindate = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_enddate = Column(VARCHAR(50))
    vc_enabled = Column(VARCHAR(1))
    vc_memo = Column(VARCHAR(2000))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_begindate)+str(self.vc_symbol_comp)+str(self.vc_symbol)+'$*'+str(self.vc_md5)