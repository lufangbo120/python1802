# coding: utf-8
from sqlalchemy import Column, DATETIME, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TInterfaceInfo(Base):
    __tablename__ = 't_interface_info'

    id = Column(INTEGER, primary_key=True)
    vc_interface_name = Column(String(50))
    vc_interface_desc = Column(String(100))
    vc_interface_tablename = Column(String(50))
    vc_interface_path = Column(String(100))
    l_files_amount = Column(INTEGER)
    c_is_header = Column(String(1))
    vc_index = Column(String(100))
    vc_python_script = Column(String(100))
    vc_remark = Column(String(100))
    d_update = Column(DATETIME)
    vc_file_type = Column(String(20))
    vc_download_path = Column(String(100))
    vc_source_file = Column(String(20))
    vc_split_sign  = Column(String(20))
    l_filetask_id = Column(INTEGER)
    vc_send_col= Column(String(255))
