# coding: utf-8
from sqlalchemy import Column, DATETIME, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TInterfaceNotice(Base):
    __tablename__ = 't_interface_notice'

    l_taskobject_id = Column(INTEGER, primary_key=True)
    vc_interface_name = Column(String(50))
    vc_interface_desc = Column(String(100))
    l_date = Column(INTEGER)
    vc_fundcode_list = Column(String(4000))
    d_start_time = Column(DATETIME)
    d_end_time = Column(DATETIME)
    c_md_status = Column(String(10))
    c_aade_status = Column(String(10))
    d_update = Column(DATETIME)

