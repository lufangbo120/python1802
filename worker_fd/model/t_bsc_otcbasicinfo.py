# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TBscOtcbasicinfo(Base):
    __tablename__ = 't_bsc_otcbasicinfo'

    l_id = Column(VARCHAR(50))
    l_publishdate = Column(VARCHAR(50))
    vc_securityid = Column(VARCHAR(20))
    vc_scode = Column(VARCHAR(20), primary_key=True)
    vc_bcode = Column(VARCHAR(20))
    vc_selfdefcode = Column(VARCHAR(10))
    l_market = Column(VARCHAR(50))
    vc_bond_code = Column(VARCHAR(10))
    c_bond_codetype = Column(CHAR(1))
    vc_bondname = Column(VARCHAR(100))
    vc_bondsname = Column(VARCHAR(40))
    vc_spellsname = Column(VARCHAR(20))
    c_bondtype = Column(CHAR(1))
    l_bondyear = Column(VARCHAR(50))
    vc_bondbatch = Column(VARCHAR(3))
    vc_issuecompcode = Column(VARCHAR(10))
    vc_issuername = Column(VARCHAR(500))
    en_maturityyear = Column(VARCHAR(50))
    en_maturityday = Column(VARCHAR(50))
    c_raisemode = Column(CHAR(1))
    vc_currency = Column(VARCHAR(10))
    en_parvalue = Column(VARCHAR(50))
    en_issueprice = Column(VARCHAR(50))
    en_initialissamt = Column(VARCHAR(50))
    en_totalissuescale = Column(VARCHAR(50))
    en_couponrate = Column(VARCHAR(50))
    l_startdate = Column(VARCHAR(50))
    l_enddate = Column(VARCHAR(50))
    l_issbegdate = Column(VARCHAR(50))
    l_issenddate = Column(VARCHAR(50))
    l_listdate = Column(VARCHAR(50))
    l_maturitydate = Column(VARCHAR(50))
    l_paymentdate = Column(VARCHAR(50))
    l_delistdate = Column(VARCHAR(50))
    l_paymentnum = Column(VARCHAR(50))
    vc_perpaydate = Column(VARCHAR(200))
    c_calcamode = Column(CHAR(1))
    c_paymentmode = Column(CHAR(1))
    en_frnspread = Column(VARCHAR(50))
    vc_exenhance = Column(VARCHAR(2))
    vc_interestrtmemo = Column(VARCHAR(2000))
    vc_baseratesecode = Column(VARCHAR(20))
    l_iscvtbd = Column(VARCHAR(50))
    vc_cvtbdtype = Column(VARCHAR(10))
    vc_cvtbdexplain = Column(VARCHAR(100))
    vc_memo = Column(VARCHAR(2000))
    l_isvalid = Column(VARCHAR(50))
    l_tmstamp = Column(VARCHAR(50))
    d_entrydate = Column(DateTime)
    vc_entrytime = Column(VARCHAR(8))
    d_src_updatetime = Column(DateTime)
    vc_data_source = Column(VARCHAR(8))
    d_updatetime = Column(DateTime)
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    l_delete = Column(VARCHAR(50), server_default=text("""\
0
"""))

    def __str__(self):
        return  str(self.vc_scode)+'$*'+str(self.vc_md5)