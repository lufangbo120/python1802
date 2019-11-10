# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscIbmminfo(Base):
    __tablename__ = 't_bsc_ibmminfo'

    vc_company_code = Column(VARCHAR(8), primary_key=True)
    l_declare_date = Column(NUMBER(8, 0, False), nullable=False)
    l_begin_date = Column(NUMBER(8, 0, False), nullable=False)
    l_end_date = Column(NUMBER(8, 0, False))
    vc_ibmm_no = Column(VARCHAR(20), nullable=False)
    vc_ibmm_name = Column(VARCHAR(200), nullable=False)
    vc_ibmm_sname = Column(VARCHAR(100))
    vc_ibmm_type = Column(VARCHAR(50))
    c_status = Column(CHAR(1))
    d_updatetime = Column(DateTime, nullable=False)
    vc_data_source = Column(VARCHAR(32), nullable=False)
    d_src_updatetime = Column(DateTime, nullable=False)
    l_source_id = Column(NUMBER(18, 0, False), nullable=False)
    c_del = Column(CHAR(1))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    l_delete = Column(NUMBER(scale=0, asdecimal=False), server_default=text("0"))

    def __str__(self):
        return  str(self.vc_company_code)+'$*'+str(self.vc_md5)