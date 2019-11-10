# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscFxrxx(Base):
    __tablename__ = 'if_bsc_fxrxx'

    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    fxrh = Column(VARCHAR(20), primary_key=True, nullable=False)
    fxfl = Column(VARCHAR(50))
    fxmc = Column(VARCHAR(80))
    fxqc = Column(VARCHAR(100))
    fxlxr = Column(VARCHAR(20))
    fxrlxdh = Column(VARCHAR(20))
    fxrcz = Column(VARCHAR(20))
    jbrxm = Column(VARCHAR(20))
    jbrzjlx = Column(VARCHAR(20))
    jbrzjhm = Column(VARCHAR(20))
    jbrlxdh = Column(VARCHAR(20))
    jbrcz = Column(VARCHAR(20))
    jbrqzwjm = Column(VARCHAR(20))
    ylqzwjm = Column(VARCHAR(20))
    fxzc = Column(VARCHAR(50))
    jbyx = Column(VARCHAR(20))
    wbpj = Column(VARCHAR(20))
    nbpj = Column(VARCHAR(20))
    zhpj = Column(VARCHAR(20))
    sxed = Column(VARCHAR(20))
    fxgj = Column(VARCHAR(30))
    zcbz = Column(VARCHAR(20))
    dbpj = Column(VARCHAR(20))
    wbpjrq = Column(VARCHAR(20))
    d_updatetime = Column(DateTime, server_default=text("sysdate"))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'fxrh'+'$*'+ 'l_date'