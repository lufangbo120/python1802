# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusPledgedrepoPool(Base):
    __tablename__ = 'if_bus_pledgedrepo_pool'

    l_date = Column(VARCHAR(40), primary_key=True, nullable=False)
    l_market = Column(NUMBER(asdecimal=False), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(8), primary_key=True, nullable=False)
    vc_name = Column(VARCHAR(100))
    vc_type = Column(VARCHAR(14))
    en_stand_code = Column(NUMBER(asdecimal=False))

    def __str__(self):
        return   'l_market'+'$*'+ 'vc_code'+'$*'+ 'l_date'