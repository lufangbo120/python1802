# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VdiPrtCashflowNew(Base):
    __tablename__ = 'vdi_prt_cashflow_new'

    key_prt_cashflow = Column(VARCHAR(50), primary_key=True)
    id_pcf_port_code = Column(VARCHAR(30))
    id_pcf_date = Column(DateTime)
    id_pcf_kind = Column(VARCHAR(30))
    pcf_share = Column(VARCHAR(50))
    pcf_asset_amount = Column(VARCHAR(50))
    pcf_port_amount = Column(VARCHAR(50))
    pcf_remark = Column(VARCHAR(120))
    pcf_rec_time = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime, server_default=text("""\
sysdate
"""))

    def __str__(self):
        return   'key_prt_cashflow'