# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTmpBscPooldataReason(Base):
    __tablename__ = 't_tmp_bsc_pooldata_reason'

    filename = Column(VARCHAR(500))
    zqdm = Column(VARCHAR(500), primary_key=True)
    type1 = Column(VARCHAR(500))
    name1 = Column(VARCHAR(500))
    scdm = Column(VARCHAR(500))
    indate = Column(VARCHAR(500))
    reason_type = Column(VARCHAR(500))
    reason_typecode = Column(VARCHAR(500))
    sname = Column(VARCHAR(500))
    remark = Column(VARCHAR(500))
