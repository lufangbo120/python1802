# coding: utf-8
from sqlalchemy import Column, DATETIME, ForeignKey, INTEGER, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TInterfaceDetailInfo(Base):
    __tablename__ = 't_interface_detail_info'

    id = Column(INTEGER, primary_key=True)
    vc_column_name = Column(String(50))
    c_add_column = Column(String(1))
    vc_addcolumn_desc = Column(String(50))
    l_interface_id = Column(INTEGER)
