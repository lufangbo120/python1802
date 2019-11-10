# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscEhrOrg(Base):
    __tablename__ = 't_bsc_ehr_org'

    vc_org_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_org_code = Column(VARCHAR(100))
    vc_org_flag = Column(VARCHAR(2), primary_key=True, nullable=False)
    vc_org_name = Column(VARCHAR(200))
    vc_parent_org_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_leader_number = Column(VARCHAR(50))
    vc_leader_name = Column(VARCHAR(200))
    vc_boss_number = Column(VARCHAR(50))
    vc_level_code = Column(VARCHAR(50))
    vc_level_name = Column(VARCHAR(200))
    vc_stamp = Column(VARCHAR(8))
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.vc_org_flag)+str(self.vc_parent_org_id)+str(self.vc_org_id)+'$*'+str(self.vc_md5)
