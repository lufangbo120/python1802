# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscFuture(Base):
    __tablename__ = 't_bsc_futures'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_contract_code = Column(VARCHAR(16), nullable=False)
    sname = Column(VARCHAR(100))
    l_market = Column(VARCHAR(50), nullable=False)
    l_contract_type = Column(VARCHAR(50), nullable=False)
    vc_option_code = Column(VARCHAR(64), nullable=False)
    en_cm_value = Column(VARCHAR(50))
    vc_underly_type = Column(VARCHAR(100))
    en_unit_quant = Column(VARCHAR(50))
    vc_order_unit = Column(VARCHAR(100))
    vc_underly_index = Column(VARCHAR(20))
    en_min_prc_chg = Column(VARCHAR(200))
    en_settle_date = Column(VARCHAR(50))
    en_minmarginratio = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_scode)+'$*'+str(self.vc_md5)