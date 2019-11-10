# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class t_node_detaillog(Base):
    __tablename__ = 't_node_detaillog'

    vc_row_uuid = Column(String(300), primary_key=True)
    l_taskobject_id = Column(Numeric(scale=0, asdecimal=False))
    vc_node_id = Column(String(100))
    vc_retcode = Column(String(100))
    vc_error_code = Column(String(100))
    vc_error_msg = Column(String(2000))
    vc_tradereference = Column(String(100))
    vc_portfoliocode = Column(String(100))
    vc_trade_type = Column(String(100))
    vc_date = Column(String(8))
    vc_file = Column(String(8))
    d_update = Column(DateTime)
