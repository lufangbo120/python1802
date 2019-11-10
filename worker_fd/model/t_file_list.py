# coding: utf-8
from sqlalchemy import Column, DATETIME, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TFileList(Base):
    __tablename__ = 't_file_list'

    id = Column(INTEGER, primary_key=True)
    vc_file_list = Column(String(2000))
    vc_sql = Column(String(2000))
    d_update = Column(DATETIME)
    l_files_amount = Column(INTEGER)
    c_flag = Column(String(1))
    c_get_list = Column(String(1))

