# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class t_node_log_aade(Base):
    __tablename__ = 't_node_log_aade'

    l_taskobject_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vc_node_id = Column(String(100))
    vc_retcode = Column(String(100))
    d_start_time = Column(DateTime)
    d_end_time = Column(DateTime)
    l_total_rows = Column(Numeric(scale=0, asdecimal=False))
    l_successful_rows = Column(Numeric(scale=0, asdecimal=False))
    l_failed_rows = Column(Numeric(scale=0, asdecimal=False))
    d_update = Column(DateTime)
