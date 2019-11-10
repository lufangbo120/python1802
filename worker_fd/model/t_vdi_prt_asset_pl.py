# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiPrtAssetPl(Base):
    __tablename__ = 't_vdi_prt_asset_pl'

    key_prt_asset_pl = Column(NUMBER(asdecimal=False), primary_key=True)
    id_pl_port_code = Column(VARCHAR(30))
    id_pl_acc_date = Column(DateTime)
    id_pl_ass_kind = Column(VARCHAR(8))
    id_pl_ass_code = Column(VARCHAR(30))
    id_pl_investment_kind = Column(VARCHAR(30))
    id_pl_pos_status = Column(VARCHAR(30))
    id_pl_asset_cur = Column(VARCHAR(10))
    id_pl_port_cur = Column(VARCHAR(10))
    id_pl_src_trans_kind = Column(VARCHAR(80))
    pl_trade_number = Column(VARCHAR(120))
    pl_trade_date = Column(DateTime)
    ass_sht_name = Column(VARCHAR(80))
    ass_lng_name = Column(VARCHAR(200))
    ass_exc_code = Column(VARCHAR(20))
    ass_custkind3 = Column(VARCHAR(20))
    ass_custkind4 = Column(VARCHAR(20))
    ass_market_code = Column(VARCHAR(30))
    pl_asset_spic = Column(NUMBER(20, 5, True))
    pl_port_spic = Column(NUMBER(20, 5, True))
    pl_asset_diic = Column(NUMBER(20, 5, True))
    pl_port_diic = Column(NUMBER(20, 5, True))
    pl_asset_inpa = Column(NUMBER(20, 5, True))
    pl_port_inpa = Column(NUMBER(20, 5, True))
    pl_asset_inic = Column(NUMBER(20, 5, True))
    pl_port_inic = Column(NUMBER(20, 5, True))
    pl_asset_exch = Column(NUMBER(20, 5, True))
    pl_port_exch = Column(NUMBER(20, 5, True))
    pl_asset_cifv = Column(NUMBER(20, 5, True))
    pl_port_cifv = Column(NUMBER(20, 5, True))
    pl_asset_laim = Column(NUMBER(20, 5, True))
    pl_port_laim = Column(NUMBER(20, 5, True))
    pl_asset_oecare = Column(NUMBER(20, 5, True))
    pl_port_oecare = Column(NUMBER(20, 5, True))
    pl_asset_fee = Column(NUMBER(20, 5, True))
    pl_port_fee = Column(NUMBER(20, 5, True))
    pl_asset_otpa = Column(NUMBER(20, 5, True))
    pl_port_otpa = Column(NUMBER(20, 5, True))
    pl_asset_otic = Column(NUMBER(20, 5, True))
    pl_port_otic = Column(NUMBER(20, 5, True))
    pl_remark = Column(VARCHAR(200))
    pl_rec_time = Column(DateTime)
    pl_asset_pyad = Column(NUMBER(20, 5, True))
    pl_port_pyad = Column(NUMBER(20, 5, True))
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.key_prt_asset_pl)+'$*'+str(self.vc_md5)