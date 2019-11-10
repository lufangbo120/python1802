# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVGp3DepoActorinfo(Base):
    __tablename__ = 't_v_gp3_depo_actorinfo'

    key_depo_actorinfo = Column(NUMBER(asdecimal=False), primary_key=True)
    id_ass_code = Column(VARCHAR(30))
    ass_sht_name = Column(VARCHAR(40))
    id_act_code = Column(VARCHAR(8))
    act_legal_country = Column(VARCHAR(13))
    rec_time = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.key_depo_actorinfo)+'$*'+str(self.vc_md5)