# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBusPledgedrepoPool(Base):
    __tablename__ = 't_bus_pledgedrepo_pool'

    l_date = Column(VARCHAR(40), primary_key=True, nullable=False)
    l_market = Column(VARCHAR(40), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(8), primary_key=True, nullable=False)
    vc_scode= Column(VARCHAR(16))
    vc_name = Column(VARCHAR(100))
    vc_type = Column(VARCHAR(14))
    en_stand_code = Column(NUMBER(asdecimal=False))
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.l_market)+str(self.vc_code)+str(self.l_date)+'$*'+str(self.vc_md5)
