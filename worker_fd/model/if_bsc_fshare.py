# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Index, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscFshare(Base):
    __tablename__ = 'if_bsc_fshare'
    __table_args__ = (
        Index('idx_vc_fshare', 'vc_code', 'l_market'),
    )

    vc_scode = Column(VARCHAR(32), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16))
    l_market = Column(VARCHAR(50))
    l_publish_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_declare_date = Column(VARCHAR(50))
    en_tradable_issuer_share = Column(VARCHAR(50))
    c_isstat = Column(CHAR(1))
    vc_chg_reason = Column(VARCHAR(100))
    en_share = Column(VARCHAR(50))
    en_untradable_issuer_share = Column(VARCHAR(50))
    en_tradable_share = Column(VARCHAR(50))
    en_public_fshare = Column(VARCHAR(50))
    en_instinvestor_share = Column(VARCHAR(50))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_publish_date'+'$*'+ 'vc_scode'