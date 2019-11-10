# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class TMd5(Base):
    __tablename__ = 't_md5s'

    vc_table_name = Column(String(300))
    l_status = Column(Numeric(scale=0, asdecimal=False))
    vc_md5 = Column(String(50),primary_key=True)

