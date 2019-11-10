# coding: utf-8
from sqlalchemy import Column, TIMESTAMP, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TOdsTl4(Base):
    __tablename__ = 't_ods_tl4'

    vc_scode = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_kind = Column(VARCHAR(20))
    vc_tl4 = Column(VARCHAR(20), primary_key=True, nullable=False)
    l_begin_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    l_end_date = Column(VARCHAR(50), primary_key=True, nullable=False)
    d_updatetime = Column(TIMESTAMP)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.vc_scode)+str(self.l_end_date)+str(self.l_begin_date)+str(self.vc_tl4)+'$*'+str(self.vc_md5)