# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfPrtPortinfo(Base):
    __tablename__ = 'if_prt_portinfo'

    vc_port_type_1 = Column(VARCHAR(1024))
    vc_port_type_2 = Column(VARCHAR(1024))
    vc_fund_name_o32 = Column(VARCHAR(1024))
    vc_insur_info = Column(VARCHAR(1024))
    vc_fund_id_o32 = Column(VARCHAR(1024))
    vc_asset_id_o32 = Column(VARCHAR(1024))
    vc_combi_name_o32 = Column(VARCHAR(1024))
    vc_combi_no_o32 = Column(VARCHAR(1024))
    vc_combi_id_o32 = Column(VARCHAR(1024))
    vc_fund_code_gp3 = Column(VARCHAR(1024))
    vc_combi_code_gp3 = Column(VARCHAR(1024))
    vc_defaule_combi = Column(VARCHAR(1024))
    vc_is_merger = Column(VARCHAR(1024))
    vc_fund_name_gp3 = Column(VARCHAR(1024))
    vc_combi_name_gp3 = Column(VARCHAR(1024))
    vc_account = Column(VARCHAR(1024))
    vc_nommanager = Column(VARCHAR(1024))
    vc_actmanager = Column(VARCHAR(1024))
    vc_invmanager = Column(VARCHAR(1024))
    vc_config = Column(VARCHAR(1024))
    vc_custodian = Column(VARCHAR(1024))
    vc_bank_account = Column(VARCHAR(1024))
    vc_invoperation = Column(VARCHAR(1024))
    vc_currency = Column(VARCHAR(1024))
    vc_summary = Column(VARCHAR(1024))
    vc_fund_code_jsz = Column(VARCHAR(1024))
    vc_fund_name_jsz = Column(VARCHAR(1024))
    vc_combi_code_hs = Column(VARCHAR(1024))
    vc_fund_code_hs = Column(VARCHAR(1024))
    vc_fund_name_web = Column(VARCHAR(1024))
    vc_fund_code_ta = Column(VARCHAR(1024))
    vc_fund_code_rep = Column(VARCHAR(1024))
    vc_fund_code_idc = Column(VARCHAR(1024))
    vc_insur_no = Column(VARCHAR(1024))
    l_serial_no = Column(VARCHAR(50), primary_key=True)
    vc_department_name = Column(VARCHAR(1024))
    vc_is_closed_accounting = Column(VARCHAR(1024))
    vc_management_type = Column(VARCHAR(1024))
    vc_crm_prod_no = Column(VARCHAR(1024))
    c_is_valid = Column(CHAR(1))
    vc_combi_department_name = Column(VARCHAR(1024))
    d_updatetime = Column(DateTime)
    l_begindata_combi = Column(VARCHAR(50))
    l_enddata_combi = Column(VARCHAR(50))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'l_serial_no'