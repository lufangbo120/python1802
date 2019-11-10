# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VdiPrtAssetTrade(Base):
    __tablename__ = 'vdi_prt_asset_trade'

    key_prt_asset_trade = Column(NUMBER(asdecimal=False), primary_key=True)
    id_pat_port_code = Column(VARCHAR(30))
    id_pat_acc_date = Column(DateTime)
    id_pat_ass_kind = Column(VARCHAR(8))
    id_pat_ass_code = Column(VARCHAR(30))
    id_pat_investment_kind = Column(VARCHAR(30))
    id_pat_pos_status = Column(VARCHAR(30))
    id_pat_trans_kind = Column(VARCHAR(30))
    id_pat_src_trans_kind = Column(VARCHAR(30))
    id_pat_asset_cur = Column(VARCHAR(10))
    id_pat_port_cur = Column(VARCHAR(10))
    pat_trade_number = Column(VARCHAR(60))
    pat_trade_date = Column(DateTime)
    ass_sht_name = Column(VARCHAR(80))
    ass_lng_name = Column(VARCHAR(200))
    ass_exc_code = Column(VARCHAR(20))
    ass_custkind3 = Column(VARCHAR(20))
    ass_custkind4 = Column(VARCHAR(20))
    ass_market_code = Column(VARCHAR(30))
    pat_share = Column(NUMBER(22, 7, True))
    pat_asset_amount = Column(NUMBER(20, 5, True))
    pat_port_amount = Column(NUMBER(20, 5, True))
    pat_asset_cost_amount = Column(NUMBER(20, 5, True))
    pat_port_cost_amount = Column(NUMBER(20, 5, True))
    pat_asset_fee = Column(NUMBER(20, 5, True))
    pat_port_fee = Column(NUMBER(20, 5, True))
    pat_asset_inre = Column(NUMBER(20, 5, True))
    pat_port_inre = Column(NUMBER(20, 5, True))
    pat_asset_acin = Column(NUMBER(20, 5, True))
    pat_port_acin = Column(NUMBER(20, 5, True))
    pat_asset_inad = Column(NUMBER(20, 5, True))
    pat_port_inad = Column(NUMBER(20, 5, True))
    pat_asset_vacg = Column(NUMBER(20, 5, True))
    pat_port_vacg = Column(NUMBER(20, 5, True))
    pat_remark = Column(VARCHAR(200))
    pat_rec_time = Column(DateTime)
    pat_port_inpa = Column(NUMBER(20, 5, True))
    pat_asset_inpa = Column(NUMBER(20, 5, True))
    pat_asset_nmv = Column(NUMBER(asdecimal=False))
    pat_port_nmv = Column(NUMBER(asdecimal=False))

    def __str__(self):
        return   'key_prt_asset_trade'