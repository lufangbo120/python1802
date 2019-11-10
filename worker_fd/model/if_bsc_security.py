# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscSecurity(Base):
    __tablename__ = 'if_bsc_security'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_code = Column(VARCHAR(16), nullable=False)
    vc_sname = Column(VARCHAR(100), nullable=False)
    vc_name = Column(VARCHAR(200))
    vc_name_en = Column(VARCHAR(200))
    vc_sname_en = Column(VARCHAR(200))
    vc_spell_abbr = Column(VARCHAR(20))
    vc_isin = Column(VARCHAR(20))
    vc_currency = Column(VARCHAR(5), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    vc_company_code = Column(VARCHAR(16))
    vc_kind = Column(VARCHAR(50), nullable=False)
    l_offer_date = Column(VARCHAR(50))
    l_list_date = Column(VARCHAR(50))
    l_cancel_date = Column(VARCHAR(50))
    c_valid_flag = Column(CHAR(1), nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_type = Column(VARCHAR(100))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_scode'