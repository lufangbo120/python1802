# coding: utf-8
from sqlalchemy import Column, DateTime, Index, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscFund(Base):
    __tablename__ = 't_bsc_fund'
    __table_args__ = (
        Index('idx_vc_fundcode', 'vc_fund_code', 'l_market'),
    )

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_fund_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_manorg_code = Column(VARCHAR(16))
    vc_manorg_name = Column(VARCHAR(256))
    vc_trusorg_code = Column(VARCHAR(16))
    vc_trusorg_name = Column(VARCHAR(256))
    en_fund_size = Column(VARCHAR(50))
    l_esti_date = Column(VARCHAR(50))
    l_list_date = Column(VARCHAR(50))
    l_open_date = Column(VARCHAR(50))
    l_mtr_date = Column(VARCHAR(50))
    l_fund_type = Column(VARCHAR(50), nullable=False)
    l_fund_investarea = Column(VARCHAR(50), nullable=False)
    l_fund_investstyle = Column(VARCHAR(50), nullable=False)
    en_fund_year = Column(VARCHAR(50))
    l_share_transfer = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    l_nav_disclosure = Column(VARCHAR(50))
    l_unit = Column(VARCHAR(50))
    l_structued = Column(VARCHAR(50))
    l_trd_loc = Column(VARCHAR(50))
    vc_fund_name = Column(VARCHAR(256))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_scode)+'$*'+str(self.vc_md5)