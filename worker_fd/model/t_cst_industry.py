# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TCstIndustry(Base):
    __tablename__ = 't_cst_industry'

    l_type_no = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_type_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_type_name = Column(VARCHAR(128), nullable=False)
    d_updatetime = Column(DateTime, nullable=False)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_type_code)+str(self.l_type_no)+'$*'+str(self.vc_md5)