# coding: utf-8
from sqlalchemy import Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTaskConfig(Base):
    __tablename__ = 't_task_config'

    id = Column(INTEGER, primary_key=True)
    vc_task_list = Column(String(500))
    vc_queue_name = Column(String(45))
    vc_routing_key = Column(String(45))
    l_task_type = Column(INTEGER)
    vc_remark = Column(String(200))
