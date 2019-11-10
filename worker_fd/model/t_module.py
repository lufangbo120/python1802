# coding: utf-8
from sqlalchemy import Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TModule(Base):
    __tablename__ = 't_module'

    id = Column(INTEGER, primary_key=True)
    vc_name = Column(String(45))
    l_type = Column(String(5))
    vc_remark = Column(String(200))
    vc_display_name = Column(String(100))
