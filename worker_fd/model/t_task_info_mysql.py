# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class t_task_info_mysql(Base):
    __tablename__ = 't_task_info_mysql'

    id = Column(Numeric(12, 0, asdecimal=False), primary_key=True)
    vc_task_name = Column(String(50))
    l_visble = Column(Numeric(11, 0, asdecimal=False))
    l_type = Column(Numeric(11, 0, asdecimal=False))
    vc_operator = Column(String(50))
    l_priority = Column(Numeric(11, 0, asdecimal=False))
    d_update = Column(DateTime)
    vc_remark = Column(String(50))
    l_datacfg_id = Column(Numeric(11, 0, asdecimal=False))
    l_interface_id = Column(Numeric(11, 0, asdecimal=False))
    l_child_task_ids = Column(String(255))
    vc_trigger_type = Column(String(5))
    l_periodic_task_id = Column(Numeric(11, 0, asdecimal=False))
    vc_begin_time = Column(String(10))
    l_source_type = Column(String(11))
    l_database_id = Column(Numeric(11, 0, asdecimal=False))
    l_script_file_id = Column(Numeric(11, 0, asdecimal=False))
