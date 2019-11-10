# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondguarantor(Base):
    __tablename__ = 'if_bsc_bondguarantor'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(VARCHAR(50), nullable=False)
    l_publish_date = Column(VARCHAR(50), nullable=False)
    vc_company_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_guarantor_name = Column(VARCHAR(128))
    l_guarantor_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_rules = Column(VARCHAR(4000))
    vc_guarantee_letter = Column(VARCHAR(4000))
    vc_claim_condition = Column(VARCHAR(100))
    vc_guarantee_beneficiary = Column(VARCHAR(30))
    en_guarantee_fee = Column(VARCHAR(50))
    vc_guarantee_contract = Column(VARCHAR(4000))
    vc_bond_issuer_zx = Column(VARCHAR(4000))
    vc_bond_pay_method = Column(VARCHAR(4000))
    en_guarant_rate = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    l_guarant_kind = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_guarantee_kind = Column(VARCHAR(50))
    l_begin_date = Column(VARCHAR(50))
    l_end_date = Column(VARCHAR(50))
    vc_guarantor_introduction = Column(VARCHAR(4000))
    vc_guarantor_scope_object = Column(VARCHAR(500))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_company_code'+'$*'+ 'l_guarantor_type'+'$*'+ 'vc_scode'+'$*'+ 'l_guarant_kind'