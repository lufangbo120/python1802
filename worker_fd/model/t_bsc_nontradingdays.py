# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscNontradingday(Base):
    __tablename__ = 't_bsc_nontradingdays'

    l_publish_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_nontrading_reason = Column(VARCHAR(3), primary_key=True, nullable=False)
    vc_nontrading_term = Column(VARCHAR(3))
    is_section = Column(CHAR(1))
    l_nontrading_begin = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_nontrading_end = Column(VARCHAR(50))
    l_retrading_day = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_data_source = Column(VARCHAR(32), nullable=False)
    d_src_updatetime = Column(DateTime, nullable=False)
    l_source_id = Column(NUMBER(18, 0, False), nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_nontrading_begin)+str(self.vc_scode)+str(self.l_publish_date)+str(self.vc_nontrading_reason)+'$*'+str(self.vc_md5)