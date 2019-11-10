# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusNonissuelockperiod(Base):
    __tablename__ = 'if_bus_nonissuelockperiod'

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
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return   'vc_report_code'+'$*'+ 'l_combi_id'+'$*'+ 'l_fund_id'