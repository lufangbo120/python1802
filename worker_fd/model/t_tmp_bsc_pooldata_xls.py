# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTmpBscPooldataXl(Base):
    __tablename__ = 't_tmp_bsc_pooldata_xls'

    filename = Column(VARCHAR(500))
    name1 = Column(VARCHAR(500))
    market = Column(VARCHAR(500))
    code = Column(VARCHAR(500), primary_key=True)
    weight = Column(VARCHAR(500))
    cp_gp = Column(VARCHAR(500))
    memo = Column(VARCHAR(500))
