# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VdiPrtPort(Base):
    __tablename__ = 'vdi_prt_port'

    key_prt_port = Column(VARCHAR(50), primary_key=True)
    id_prt_code = Column(VARCHAR(30))
    id_prt_srcsys = Column(VARCHAR(10))
    prt_parent_code = Column(VARCHAR(30))
    prt_sht_name = Column(VARCHAR(40))
    prt_lng_name = Column(VARCHAR(200))
    prt_inception_date = Column(DateTime)
    prt_maturity_date = Column(DateTime)
    prt_cur_code = Column(VARCHAR(10))
    prt_kind = Column(VARCHAR(30))
    prt_src_rec_key = Column(VARCHAR(30))
    prt_acc_chart = Column(VARCHAR(30))
    prt_client = Column(VARCHAR(60))
    prt_trustee = Column(VARCHAR(60))
    prt_investment_manager = Column(VARCHAR(60))
    prt_etl_bgndate = Column(DateTime)
    prt_department = Column(VARCHAR(30))
    prt_stgy = Column(VARCHAR(30))
    rpt_rec_time = Column(DateTime)
    prt_etl_netsrc = Column(VARCHAR(50))
    prt_prod_regno = Column(VARCHAR(60))
    prt_prod_kind_code = Column(VARCHAR(60))
    prt_prod_kind_name = Column(VARCHAR(200))
    prt_prod_code = Column(VARCHAR(30))
    prt_prod_sht_name = Column(VARCHAR(200))
    prt_prod_lng_name = Column(VARCHAR(200))
    prt_prod_setup_date = Column(DateTime)
    prt_rnav_flag = Column(VARCHAR(30))
    prt_nosubport_date = Column(DateTime)
    prt_clear_acc_date = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return   'key_prt_port'