# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscFundinfo(Base):
    __tablename__ = 't_bsc_fundinfo'

    l_fund_id = Column(NUMBER(10, 0, False), primary_key=True)
    vc_fund_code = Column(VARCHAR(16), nullable=False)
    vc_fund_name = Column(VARCHAR(64))
    l_default_asset = Column(NUMBER(8, 0, False))
    l_default_combi = Column(NUMBER(12, 0, False))
    c_fund_type = Column(CHAR(1))
    c_fund_status = Column(CHAR(1))
    l_bank_id = Column(NUMBER(10, 0, False))
    vc_bank_account = Column(VARCHAR(30))
    vc_shclearing_account = Column(VARCHAR(30))
    l_main_fund_id = Column(NUMBER(4, 0, False))
    vc_mkt_fund_code = Column(VARCHAR(16))
    c_fund_type2 = Column(CHAR(4))
    vc_fund_tag = Column(VARCHAR(8))
    iscurrmngpdt = Column(VARCHAR(32))
    vc_sequare_code = Column(VARCHAR(128))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.l_fund_id)+'$*'+str(self.vc_md5)