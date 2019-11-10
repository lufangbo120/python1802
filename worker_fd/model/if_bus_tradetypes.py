# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBusTradetype(Base):
    __tablename__ = 'if_bus_tradetypes'

    l_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_serial_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    c_trade_type = Column(CHAR(1), nullable=False)
    l_parent_id = Column(NUMBER(8, 0, False), nullable=False)
    l_fund_id = Column(NUMBER(4, 0, False), nullable=False)
    vc_trade_no = Column(VARCHAR(32), nullable=False)
    vc_trade_name = Column(VARCHAR(128))
    c_trade_status = Column(CHAR(1))
    vc_remarks = Column(VARCHAR(64))
    en_trade_power = Column(VARCHAR(50))
    l_root_id = Column(NUMBER(8, 0, False))
    c_stockpool_type = Column(CHAR(1))
    l_dimlayer_id = Column(NUMBER(10, 0, False))
    d_updatetime = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_serial_id'+'$*'+ 'l_date'