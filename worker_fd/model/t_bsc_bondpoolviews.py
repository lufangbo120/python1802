# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscBondpoolview(Base):
    __tablename__ = 't_bsc_bondpoolviews'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_name = Column(VARCHAR(100))
    l_market = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16), nullable=False)
    l_date = Column(NUMBER(8, 0, False), primary_key=True, nullable=False)
    vc_companyname = Column(VARCHAR(64))
    l_guarant_kind = Column(VARCHAR(50))
    vc_poolname = Column(VARCHAR(20))
    vc_innercompany_rank = Column(VARCHAR(20))
    vc_companycredit_rank = Column(VARCHAR(20))
    vc_innerbond_rank = Column(VARCHAR(200))
    vc_bondcredit_rank = Column(VARCHAR(20))
    vc_rankwatch = Column(VARCHAR(20))
    l_credit_anticipate = Column(VARCHAR(50))
    vc_companylongratename = Column(VARCHAR(64))
    vc_industryname_tk = Column(VARCHAR(64))
    vc_company_type = Column(VARCHAR(128))
    vc_bond_type = Column(VARCHAR(64))
    c_is_vrcode = Column(CHAR(1))
    c_is_compliance = Column(CHAR(1))
    c_is_highrisk = Column(CHAR(1))
    vc_focustype = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)
    vc_bond_highrisk = Column(VARCHAR(10))
    vc_bb_bond_highrisk = Column(VARCHAR(10))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_market)+str(self.l_date)+str(self.vc_scode)+'$*'+str(self.vc_md5)