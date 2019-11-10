# coding: utf-8
from sqlalchemy import Column, DATETIME, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TStatus(Base):
    __tablename__ = 't_status'

    l_taskid = Column(INTEGER, primary_key=True)
    l_status = Column(INTEGER)
    l_child_id = Column(INTEGER)
