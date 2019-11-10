# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscPfNav(Base):
    __tablename__ = 't_bsc_pf_nav'

    vc_pf_code = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_enddate = Column(VARCHAR(50), primary_key=True, nullable=False)
    en_unitnav = Column(VARCHAR(50))
    en_unitaccnav = Column(VARCHAR(50))
    en_repairunitnav = Column(VARCHAR(50))
    en_navgrtd = Column(VARCHAR(50))
    en_navgrl1w = Column(VARCHAR(50))
    en_navgrt1w = Column(VARCHAR(50))
    en_navgrl1m = Column(VARCHAR(50))
    en_navgrt1m = Column(VARCHAR(50))
    en_navgrl3m = Column(VARCHAR(50))
    en_navgrtq = Column(VARCHAR(50))
    en_navgrl6m = Column(VARCHAR(50))
    en_navgrts = Column(VARCHAR(50))
    en_navgrl1y = Column(VARCHAR(50))
    en_navgrt1y = Column(VARCHAR(50))
    en_navgrlist = Column(VARCHAR(50))
    l_isvalid = Column(NUMBER(1, 0, False))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_pf_code)+str(self.l_enddate)+'$*'+str(self.vc_md5)