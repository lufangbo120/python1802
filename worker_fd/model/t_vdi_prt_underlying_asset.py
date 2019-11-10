# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TVdiPrtUnderlyingAsset(Base):
    __tablename__ = 't_vdi_prt_underlying_asset'

    key_prt_underlying_asset = Column(NUMBER(asdecimal=False), primary_key=True)
    una_ass_kind = Column(VARCHAR(30))
    una_ass_code = Column(VARCHAR(30))
    una_underlying_ass_kind = Column(VARCHAR(30))
    una_underlying_ass_code = Column(VARCHAR(30))
    una_start_date = Column(DateTime)
    una_end_date = Column(DateTime)
    una_share_par = Column(NUMBER(22, 7, True))
    una_principal = Column(NUMBER(20, 5, True))
    una_src_rec_key = Column(NUMBER(asdecimal=False))
    una_rec_time = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))

    def __str__(self):
        return  str(self.key_prt_underlying_asset)+'$*'+str(self.vc_md5)