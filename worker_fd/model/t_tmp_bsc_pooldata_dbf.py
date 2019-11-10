# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTmpBscPooldataDbf(Base):
    __tablename__ = 't_tmp_bsc_pooldata_dbf'

    filename = Column(VARCHAR(500))
    code = Column(VARCHAR(500), primary_key=True)
    type1 = Column(VARCHAR(500))
    name1 = Column(VARCHAR(500))
    market = Column(VARCHAR(500))
    isocode = Column(VARCHAR(1000))
    type2 = Column(VARCHAR(500))
    name2 = Column(VARCHAR(500))
    type3 = Column(VARCHAR(500))
    name3 = Column(VARCHAR(500))
    type4 = Column(VARCHAR(500))
    name4 = Column(VARCHAR(500))
