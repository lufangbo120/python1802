# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscBonduwrt(Base):
    __tablename__ = 't_bsc_bonduwrt'

    vc_scode = Column(VARCHAR(14), primary_key=True, nullable=False)
    vc_underwriter_code = Column(VARCHAR(8), primary_key=True, nullable=False)
    vc_underwriter_name = Column(VARCHAR(100))
    vc_underwriter_type = Column(VARCHAR(30), primary_key=True, nullable=False)
    en_underwriting_quantity = Column(VARCHAR(50))
    en_underwriting_ratio = Column(VARCHAR(50))
    en_package_money = Column(VARCHAR(50))
    en_commission_rate = Column(VARCHAR(50))
    en_commission_money = Column(VARCHAR(50))
    vc_memo = Column(VARCHAR(1024))
    d_declaredate = Column(DateTime)
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_code = Column(VARCHAR(20), nullable=False)
    l_market = Column(VARCHAR(50))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_underwriter_type)+str(self.vc_scode)+str(self.vc_underwriter_code)+'$*'+str(self.vc_md5)