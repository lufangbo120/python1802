# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscPfBasicinfo(Base):
    __tablename__ = 'if_bsc_pf_basicinfo'

    l_declare_date = Column(VARCHAR(50))
    vc_pf_code = Column(VARCHAR(20), primary_key=True)
    vc_fp_sname = Column(VARCHAR(100))
    vc_fp_name = Column(VARCHAR(200))
    vc_exchange = Column(VARCHAR(10))
    l_currency = Column(VARCHAR(50))
    vc_classcode1 = Column(VARCHAR(10))
    vc_classcode2 = Column(VARCHAR(10))
    vc_investmethod = Column(VARCHAR(10))
    vc_investdirection = Column(VARCHAR(10))
    l_salebegin_date = Column(VARCHAR(50))
    l_saleend_date = Column(VARCHAR(50))
    l_found_date = Column(VARCHAR(50))
    l_enddate = Column(VARCHAR(50))
    l_duration = Column(NUMBER(10, 0, False))
    vc_durationunit = Column(VARCHAR(10))
    en_issamt = Column(VARCHAR(50))
    en_exptyield = Column(VARCHAR(50))
    en_minsubamt = Column(VARCHAR(50))
    l_pretotshare = Column(NUMBER(10, 0, False))
    l_parvalue = Column(VARCHAR(50))
    vc_srstatus = Column(VARCHAR(200))
    vc_recordcompcode = Column(VARCHAR(8))
    vc_trustcompcode = Column(VARCHAR(8))
    vc_manacompcode = Column(VARCHAR(8))
    vc_managername = Column(VARCHAR(100))
    vc_fpsn = Column(VARCHAR(12))
    l_isvalid = Column(NUMBER(1, 0, False))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_pf_code'