# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscBondforbiddenpool(Base):
    __tablename__ = 'if_bsc_bondforbiddenpool'

    vc_bond_code = Column(VARCHAR(20), primary_key=True, nullable=False)
    vc_dimensions_code = Column(VARCHAR(10))
    vc_dimensions_name = Column(VARCHAR(100))
    l_market = Column(VARCHAR(50))
    d_indate = Column(DateTime, primary_key=True, nullable=False)
    vc_typecode = Column(VARCHAR(10), primary_key=True, nullable=False)
    vc_bond_name = Column(VARCHAR(500))
    vc_remark = Column(VARCHAR(4000))
    d_updatetime = Column(DateTime)
    d_src_updatetime = Column(DateTime)
    vc_data_source = Column(VARCHAR(8))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_bond_code'+'$*'+ 'vc_typecode'+'$*'+ 'd_indate'