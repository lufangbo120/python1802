# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscPenmngPdct(Base):
    __tablename__ = 't_bsc_penmng_pdct'

    vc_innercode = Column(VARCHAR(20), nullable=True)
    vc_outercode = Column(VARCHAR(16),  nullable=True)
    vc_name = Column(VARCHAR(256))
    vc_sname = Column(VARCHAR(128))
    vc_product = Column(VARCHAR(12))
    vc_product_type = Column(VARCHAR(10))
    vc_style = Column(VARCHAR(1024))
    l_market = Column(NUMBER(asdecimal=False))
    vc_company_code = Column(VARCHAR(16))
    vc_md5 = Column(VARCHAR(32),primary_key=True)

    def __str__(self):
        return  str(self.vc_innercode)+str(self.vc_outercode)+'$*'+str(self.vc_md5)
