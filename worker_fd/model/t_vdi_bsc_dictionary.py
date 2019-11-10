# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiBscDictionary(Base):
    __tablename__ = 't_vdi_bsc_dictionary'

    key_bsc_dictionary = Column(VARCHAR(50), primary_key=True)
    id_dic_code = Column(VARCHAR(30))
    id_dic_rec_enddate = Column(DateTime)
    dic_rec_bgndate = Column(DateTime)
    dic_sht_name = Column(VARCHAR(100))
    dic_lng_name = Column(VARCHAR(200))
    dic_src_rec_key = Column(VARCHAR(100))
    dic_rec_time = Column(DateTime)
    dic_remark = Column(VARCHAR(200))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.key_bsc_dictionary)+'$*'+str(self.vc_md5)