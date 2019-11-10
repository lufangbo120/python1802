# coding: utf-8
from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VOrgUser(Base):
    __tablename__ = 'v_org_user'

    vc_level_code = Column(VARCHAR(50))
    vc_org1_id = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_org1_name = Column(VARCHAR(600))
    vc_boss_number = Column(VARCHAR(50))
    vc_boss_loginname = Column(VARCHAR(50))
    vc_boss_usernname = Column(VARCHAR(200))
    vc_org2_code = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_org2_name = Column(VARCHAR(600))
    vc_leader_number = Column(VARCHAR(50))
    vc_leader_loginname = Column(VARCHAR(50))
    vc_leader_name = Column(VARCHAR(200))
    vc_user_number = Column(VARCHAR(20))
    vc_loginname = Column(VARCHAR(50), primary_key=True, nullable=False)
    vc_username = Column(VARCHAR(200))
    vc_job_name = Column(VARCHAR(300),primary_key=True)
    l_contains = Column(VARCHAR(50))

    def __str__(self):
        return   'vc_org1_id'+'$*'+ 'vc_job_name'+'$*'+ 'vc_org2_code'+'$*'+ 'vc_loginname'
