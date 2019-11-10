# coding: utf-8
from sqlalchemy import Column, DateTime, Index, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VdiPrtAssetDetailed(Base):
    __tablename__ = 'vdi_prt_asset_detailed'
    __table_args__ = (
        Index('a', 'ass_custkind4', 'id_pad_port_code', 'id_pad_date'),
        Index('c', 'id_pad_ass_kind', 'ass_custkind4', 'id_pad_port_code', 'id_pad_date'),
        Index('b', 'id_pad_ass_kind', 'id_pad_port_code', 'id_pad_date')
    )

    key_prt_asset_detailed = Column(VARCHAR(50), primary_key=True)
    id_pad_stock = Column(VARCHAR(8))
    id_pad_port_code = Column(VARCHAR(30))
    id_pad_date = Column(DateTime)
    id_pad_ass_kind = Column(VARCHAR(8))
    id_pad_ass_code = Column(VARCHAR(30))
    id_pad_investment_kind = Column(VARCHAR(30))
    id_pad_pos_status = Column(VARCHAR(30))
    pad_asset_cur = Column(VARCHAR(10))
    pad_port_cur = Column(VARCHAR(10))
    pad_src_rec_key = Column(VARCHAR(30))
    pad_share = Column(VARCHAR(50))
    pad_asset_orig_cost = Column(VARCHAR(50))
    pad_port_orig_cost = Column(VARCHAR(50))
    pad_asset_inte_adju = Column(VARCHAR(50))
    pad_port_inte_adju = Column(VARCHAR(50))
    pad_asset_inte_rece = Column(VARCHAR(50))
    pad_port_inte_rece = Column(VARCHAR(50))
    pad_asset_fair_value = Column(VARCHAR(50))
    pad_port_fair_value = Column(VARCHAR(50))
    pad_asset_full_value = Column(VARCHAR(50))
    pad_port_full_value = Column(VARCHAR(50))
    pad_asset_dimi_value = Column(VARCHAR(50))
    pad_port_dimi_value = Column(VARCHAR(50))
    pad_rec_time = Column(DateTime)
    pad_asset_full_cost = Column(VARCHAR(50))
    pad_port_full_cost = Column(VARCHAR(50))
    ass_sht_name = Column(VARCHAR(40))
    ass_lng_name = Column(VARCHAR(200))
    ass_market_code = Column(VARCHAR(30))
    ass_issuer_code = Column(VARCHAR(30))
    ass_issuer_name = Column(VARCHAR(100))
    ass_issue_cur = Column(VARCHAR(10))
    ass_face_value = Column(VARCHAR(50))
    ass_subkind = Column(VARCHAR(30))
    ass_custkind3 = Column(VARCHAR(30))
    ass_custkind4 = Column(VARCHAR(30))
    ass_exc_code = Column(VARCHAR(8))
    ass_issue_date = Column(DateTime)
    pad_asset_inte_rece_a = Column(VARCHAR(50))
    pad_asset_inte_rece_b = Column(VARCHAR(50))
    pad_port_inte_rece_a = Column(VARCHAR(50))
    pad_port_inte_rece_b = Column(VARCHAR(50))
    pad_investment_kind_en = Column(VARCHAR(30))
    key_etl_instruction = Column(VARCHAR(50))
    ass_subtype = Column(VARCHAR(30))
    ass_start_date = Column(DateTime)
    ass_maturity_date = Column(DateTime)
    ass_rate_receive = Column(VARCHAR(50))
    ass_coupon_frequency = Column(VARCHAR(50))
    ass_accrual_method = Column(VARCHAR(30))
    ass_rate_type_receive = Column(VARCHAR(30))
    pad_asset_contract_cost = Column(VARCHAR(50))
    pad_port_contract_cost = Column(VARCHAR(50))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime, server_default=text("""\
sysdate
"""))

    def __str__(self):
        return   'key_prt_asset_detailed'