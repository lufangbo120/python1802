# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscNtsLiqDi(Base):
    __tablename__ = 't_bsc_nts_liq_dis'

    l_date = Column(NUMBER(scale=0, asdecimal=False), primary_key=True)
    vc_scode = Column(VARCHAR(22))
    vc_code = Column(VARCHAR(20))
    l_market = Column(NUMBER(scale=0, asdecimal=False))
    l_end_date = Column(NUMBER(scale=0, asdecimal=False))
    l_publish_date = Column(NUMBER(scale=0, asdecimal=False))
    vc_type_name = Column(VARCHAR(200))
    vc_type_code = Column(VARCHAR(50))
    l_ltshare_date = Column(NUMBER(scale=0, asdecimal=False))
    en_risk = Column(NUMBER(asdecimal=False))
    d_updatetime = Column(DateTime)
    vc_data_source = Column(VARCHAR(10))

    def __str__(self):
        return  str(self.l_date)+'$*'+str(self.vc_md5)