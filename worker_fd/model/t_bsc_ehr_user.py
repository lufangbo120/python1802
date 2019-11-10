# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscEhrUser(Base):
    __tablename__ = 't_bsc_ehr_user'

    vc_base_name = Column(VARCHAR(50))
    vc_base_code = Column(VARCHAR(3))
    vc_org_code = Column(VARCHAR(50))
    vc_org_name = Column(VARCHAR(50))
    vc_org2_code = Column(VARCHAR(50))
    vc_org2_name = Column(VARCHAR(300))
    vc_loginname = Column(VARCHAR(50))
    vc_loginpassword = Column(VARCHAR(50))
    vc_username = Column(VARCHAR(200))
    vc_job_id = Column(VARCHAR(50))
    vc_job_name = Column(VARCHAR(300))
    vc_user_number = Column(VARCHAR(20))
    vc_email = Column(VARCHAR(50))
    vc_gender_cdoe = Column(VARCHAR(50))
    vc_gender_name = Column(VARCHAR(50))
    vc_role_code = Column(VARCHAR(50))
    vc_role_name = Column(VARCHAR(200))
    vc_status = Column(VARCHAR(50))
    vc_stamp = Column(VARCHAR(8))
    vc_unique_id = Column(VARCHAR(38), primary_key=True)
    d_sdate = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.vc_unique_id)+'$*'+str(self.vc_md5)
