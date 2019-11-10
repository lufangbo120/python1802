# coding: utf-8
from sqlalchemy import Column, DateTime, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTaskInfo(Base):
    __tablename__ = 't_task_info'

    id = Column(INTEGER, primary_key=True)
    vc_task_name = Column(String(50))
    l_visble = Column(INTEGER)
    l_type = Column(INTEGER)
    vc_operator = Column(String(50))
    l_priority = Column(INTEGER)
    d_update = Column(DateTime)
    vc_remark = Column(String(50))
    l_datacfg_id = Column(INTEGER, index=True)
    l_interface_id = Column(INTEGER, index=True)
    l_child_task_ids = Column(String(255))
    vc_trigger_type = Column(String(5))
    l_periodic_task_id = Column(INTEGER)
    vc_begin_time = Column(String(10))
