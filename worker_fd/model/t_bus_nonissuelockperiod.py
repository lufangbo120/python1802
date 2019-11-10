# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBusNonissuelockperiod(Base):
    __tablename__ = 't_bus_nonissuelockperiod'

    l_fund_id = Column(NUMBER(10, 0, False), primary_key=True, nullable=False)
    vc_report_code = Column(VARCHAR(16), primary_key=True, nullable=False)
    vc_report_name = Column(VARCHAR(32))
    l_begin_date = Column(NUMBER(8, 0, False), nullable=False)
    l_end_date = Column(NUMBER(8, 0, False), nullable=False)
    vc_type = Column(VARCHAR(32))
    en_amount = Column(VARCHAR(50))
    en_unitcost = Column(VARCHAR(50))
    l_lockdays = Column(VARCHAR(50))
    l_combi_id = Column(NUMBER(12, 0, False), primary_key=True, nullable=False)
    l_date = Column(NUMBER(8, 0, False))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.vc_report_code)+str(self.l_combi_id)+str(self.l_fund_id)+'$*'+str(self.vc_md5)