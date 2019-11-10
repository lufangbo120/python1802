# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class t_node(Base):
    __tablename__ = 't_node'

    l_taskobject_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    vc_interface_name = Column(String(300))
    vc_interface_desc = Column(String(1000))
    vc_date = Column(String(8))
    vc_fundcode_list = Column(Text)
    d_start_time = Column(DateTime)
    d_end_time = Column(DateTime)
    vc_md_status = Column(String(10))
    vc_aade_status = Column(String(10))
    vc_group_code = Column(String(4000))
    d_update = Column(DateTime)
