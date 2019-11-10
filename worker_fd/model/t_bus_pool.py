# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBusPool(Base):
    __tablename__ = 't_bus_pool'

    l_serial_id = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    vc_inter_code = Column(VARCHAR(8), nullable=False)
    l_date = Column(NUMBER(scale=0, asdecimal=False), primary_key=True, nullable=False)
    en_stock_power = Column(NUMBER(32, 8, True), nullable=False)
    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(NUMBER(scale=0, asdecimal=False), nullable=False)
    c_contain = Column(CHAR(1), server_default=text("0"))
    l_operator_no = Column(NUMBER(scale=0, asdecimal=False))
    l_add_date = Column(NUMBER(scale=0, asdecimal=False))
    l_add_time = Column(NUMBER(scale=0, asdecimal=False))
    l_near_amount = Column(NUMBER(scale=0, asdecimal=False))
    l_begin_date = Column(NUMBER(scale=0, asdecimal=False), nullable=False, server_default=text("0 "))
    l_end_date = Column(NUMBER(scale=0, asdecimal=False), nullable=False, server_default=text("0 "))
    l_check_operator = Column(NUMBER(scale=0, asdecimal=False))
    vc_remarks = Column(VARCHAR(1024))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.l_serial_id)+str(self.vc_scode)+str(self.l_date)+'$*'+str(self.vc_md5)