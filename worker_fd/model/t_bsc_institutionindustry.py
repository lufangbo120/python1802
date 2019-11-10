# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Unicode, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscInstitutionindustry(Base):
    __tablename__ = 't_bsc_institutionindustry'

    vc_company_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_type_no = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_english_name = Column(VARCHAR(500))
    vc_one_code = Column(VARCHAR(50))
    vc_one_name = Column(VARCHAR(100))
    vc_two_code = Column(VARCHAR(50))
    vc_two_name = Column(VARCHAR(100))
    vc_three_code = Column(VARCHAR(50))
    vc_three_name = Column(VARCHAR(100))
    vc_four_code = Column(VARCHAR(50))
    vc_four_name = Column(VARCHAR(100))
    c_new_equity = Column(CHAR(1))
    c_first_income = Column(CHAR(1))
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(Unicode(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.l_end_date)+str(self.l_begin_date)+str(self.vc_company_code)+str(self.l_type_no)+'$*'+str(self.vc_md5)