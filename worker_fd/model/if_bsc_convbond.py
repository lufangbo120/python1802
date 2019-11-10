# coding: utf-8
from sqlalchemy import Column, DateTime, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscConvbond(Base):
    __tablename__ = 'if_bsc_convbond'

    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_bond_code = Column(VARCHAR(16), nullable=False)
    l_market = Column(NUMBER(scale=0, asdecimal=False), nullable=False)
    en_redeem_interest = Column(NUMBER(20, 8, True))
    vc_equity_code = Column(VARCHAR(20))
    l_convert_bdate = Column(NUMBER(scale=0, asdecimal=False))
    l_convert_edate = Column(NUMBER(scale=0, asdecimal=False))
    en_convert_ratio = Column(NUMBER(20, 6, True))
    en_convert_price = Column(NUMBER(20, 6, True))
    cl_convert_clause = Column(Text)
    d_updatetime = Column(DateTime, nullable=False)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    l_delete = Column(NUMBER(scale=0, asdecimal=False), server_default=text("""\
0
"""))

    def __str__(self):
        return   'vc_scode'