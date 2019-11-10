# coding: utf-8
from sqlalchemy import Column, INTEGER, String, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TDataConfigInfo(Base):
    __tablename__ = 't_dataconfig_info'

    id = Column(INTEGER, primary_key=True)
    vc_name = Column(String(50))
    vc_table_name = Column(String(50))
    vc_sql = Column(TEXT)
    vc_column = Column(TEXT)
    vc_index = Column(String(255))
    vc_task_ids = Column(String(255))
