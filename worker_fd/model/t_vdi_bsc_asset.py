# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiBscAsset(Base):
    __tablename__ = 't_vdi_bsc_asset'

    key_bsc_asset = Column(VARCHAR(50), primary_key=True)
    id_ass_kind = Column(VARCHAR(30))
    id_ass_code = Column(VARCHAR(30))
    ass_sht_name = Column(VARCHAR(40))
    ass_lng_name = Column(VARCHAR(200))
    ass_market_code = Column(VARCHAR(30))
    ass_exc_code = Column(VARCHAR(8))
    ass_issuer_code = Column(VARCHAR(30))
    ass_issuer_name = Column(VARCHAR(90))
    ass_issue_cur = Column(VARCHAR(10))
    ass_face_value = Column(VARCHAR(50))
    ass_src_rec_key = Column(VARCHAR(30))
    ass_subkind = Column(VARCHAR(30))
    ass_subtype = Column(VARCHAR(30))
    ass_custkind1 = Column(VARCHAR(30))
    ass_custkind2 = Column(VARCHAR(30))
    ass_custkind3 = Column(VARCHAR(30))
    ass_custkind4 = Column(VARCHAR(30))
    ass_start_date = Column(DateTime)
    ass_maturity_date = Column(DateTime)
    ass_rate_receive = Column(VARCHAR(50))
    ass_coupon_frequency = Column(VARCHAR(50))
    ass_accrual_method = Column(VARCHAR(30))
    ass_rate_type_receive = Column(VARCHAR(30))
    ass_rec_time = Column(DateTime)
    ass_issue_date = Column(DateTime)
    ass_callable_start_date = Column(DateTime)
    ass_putable_start_date = Column(DateTime)
    ass_coupon_anniv_date = Column(DateTime)
    ass_callable_flag = Column(VARCHAR(4))
    ass_putable_flag = Column(VARCHAR(4))
    ass_subtype_ref = Column(VARCHAR(30))
    ass_deposit_break_date = Column(DateTime)
    ass_underlying_code = Column(VARCHAR(30))
    ocr_id_translation = Column(VARCHAR(21))
    ocr_id_translation_name = Column(VARCHAR(100))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return  str(self.key_bsc_asset)+'$*'+str(self.vc_md5)