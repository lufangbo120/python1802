# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscStockboard(Base):
    __tablename__ = 't_bsc_stockboard'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_changebegin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_changeend_date = Column(VARCHAR(50))
    vc_company_code = Column(VARCHAR(16))
    l_board_code = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_board_name = Column(VARCHAR(64))
    vc_key_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_key_name = Column(VARCHAR(64))
    l_valid_code = Column(VARCHAR(50))
    d_src_updatetime = Column(DateTime)
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_key_code)+str(self.l_changebegin_date)+str(self.vc_scode)+str(self.l_board_code)+'$*'+str(self.vc_md5)