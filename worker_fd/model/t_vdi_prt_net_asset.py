# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiPrtNetAsset(Base):
    __tablename__ = 't_vdi_prt_net_asset'

    key_prt_net_asset = Column(VARCHAR(50), primary_key=True)
    id_pna_port_code = Column(VARCHAR(30))
    id_pna_valuation_date = Column(DateTime)
    pna_src_rec_key = Column(VARCHAR(30))
    pna_total_value = Column(VARCHAR(50))
    pna_total_share = Column(VARCHAR(50))
    pna_nav = Column(VARCHAR(50))
    pna_sub_share = Column(VARCHAR(50))
    pna_red_share = Column(VARCHAR(50))
    pna_sub_amount = Column(VARCHAR(50))
    pna_red_amount = Column(VARCHAR(50))
    pna_rec_time = Column(DateTime)
    pna_total_asset = Column(VARCHAR(50))
    pna_accumulated_nav = Column(VARCHAR(50))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime, server_default=text("""\
sysdate
"""))

    def __str__(self):
        return  str(self.key_prt_net_asset)+'$*'+str(self.vc_md5)