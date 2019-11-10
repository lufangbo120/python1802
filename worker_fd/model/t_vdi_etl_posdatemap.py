# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiEtlPosdatemap(Base):
    __tablename__ = 't_vdi_etl_posdatemap'

    key_etl_posdatemap = Column(VARCHAR(50), primary_key=True)
    pdm_port_code = Column(VARCHAR(60))
    pdm_map_date = Column(DateTime)
    pdm_pos_date = Column(DateTime)
    pdm_valid_flag = Column(VARCHAR(50))
    pdm_rec_time = Column(DateTime)
    pdm_remark = Column(VARCHAR(200))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.key_etl_posdatemap)+'$*'+str(self.vc_md5)