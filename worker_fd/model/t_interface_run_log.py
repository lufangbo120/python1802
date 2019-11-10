# coding: utf-8
from sqlalchemy import Column, DATETIME, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Trunlog(Base):
    __tablename__ = 't_interface_run_log'

    id = Column(INTEGER, primary_key=True)
    l_run_date = Column(INTEGER)
    c_run_status = Column(String(1))

