# coding: utf-8
from sqlalchemy import Column, DateTime, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTaskobjectInfo(Base):
    __tablename__ = 't_taskobject_info'

    id = Column(INTEGER, primary_key=True)
    l_run_date = Column(INTEGER)
    d_begin_time = Column(DateTime)
    d_end_time = Column(DateTime)
    vc_run_status = Column(String(50))
    vc_operator = Column(String(50))
    vc_remark = Column(String(50))
    vc_file_path = Column(String(50))
    l_task_id = Column(INTEGER, nullable=False, index=True)
    vc_uuid = Column(String(50))
    vc_parameter = Column(String(2000))
    l_is_show = Column(INTEGER)
