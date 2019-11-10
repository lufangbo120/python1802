# coding: utf-8
from sqlalchemy import Column, DATETIME, ForeignKey, INTEGER, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TMessInfo(Base):
    __tablename__ = 't_mess_info'

    id = Column(INTEGER, primary_key=True)
    vc_task_name = Column(String(50))
    l_send = Column(INTEGER)
    vc_cre_sql = Column(String(500))
    vc_up_sql = Column(String(500))
    vc_del_sql = Column(String(500))
