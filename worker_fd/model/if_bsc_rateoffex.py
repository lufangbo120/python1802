# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscRateoffex(Base):
    __tablename__ = 'if_bsc_rateoffex'

    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_price_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_price = Column(VARCHAR(50), nullable=False)
    l_info_source = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_pcurrency = Column(VARCHAR(3), primary_key=True, nullable=False)
    vc_excurrency = Column(VARCHAR(3), primary_key=True, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_info_source'+'$*'+ 'l_date'+'$*'+ 'vc_excurrency'+'$*'+ 'vc_pcurrency'+'$*'+ 'l_price_type'