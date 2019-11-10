# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscInstitutioncredit(Base):
    __tablename__ = 'if_bsc_institutioncredit'

    vc_company_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_ratecompany_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_ratecompany_name = Column(VARCHAR(256))
    l_credit_type = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_credit_rank = Column(VARCHAR(16))
    l_credit_anticipate = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_company_code'+'$*'+ 'l_begin_date'+'$*'+ 'l_end_date'+'$*'+ 'vc_ratecompany_code'+'$*'+ 'l_credit_type'