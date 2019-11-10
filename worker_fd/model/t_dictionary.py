# coding: utf-8
from sqlalchemy import Column, INTEGER, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TDictionary(Base):
    __tablename__ = 't_dictionary'

    id = Column(INTEGER, primary_key=True)
    l_dictionary_no = Column(INTEGER)
    vc_lemma_item = Column(String(10))
    vc_item_name = Column(String(50))
    vc_remark = Column(String(255))
