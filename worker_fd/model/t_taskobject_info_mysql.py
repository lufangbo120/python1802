# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class t_taskobject_info_mysql(Base):
    __tablename__ = 't_taskobject_info_mysql'

    id = Column(Numeric(11, 0, asdecimal=False), primary_key=True)
    l_run_date = Column(Numeric(11, 0, asdecimal=False))
    d_begin_time = Column(DateTime)
    d_end_time = Column(DateTime)
    vc_run_status = Column(String(50))
    vc_operator = Column(String(50))
    vc_remark = Column(String(50))
    vc_file_path = Column(String(50))
    l_task_id = Column(Numeric(11, 0, asdecimal=False))
    vc_uuid = Column(String(50))
    l_is_show = Column(Numeric(1, 0, asdecimal=False))
