# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscSharecapitalstructure(Base):
    __tablename__ = 'if_bsc_sharecapitalstructure'

    vc_company_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_total_share = Column(VARCHAR(50))
    en_total_tradableshare = Column(VARCHAR(50))
    en_tshare_a = Column(VARCHAR(50))
    en_tshare_b = Column(VARCHAR(50))
    en_tshare_h = Column(VARCHAR(50))
    en_ltshare_a = Column(VARCHAR(50))
    en_ltshare_b = Column(VARCHAR(50))
    en_ltshare_h = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_company_code'+'$*'+ 'l_date'