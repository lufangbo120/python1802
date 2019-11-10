# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, Float, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class IfBscInstitutionprofile(Base):
    __tablename__ = 'if_bsc_institutionprofile'

    vc_company_code = Column(VARCHAR(16), primary_key=True)
    vc_parent_company = Column(VARCHAR(16), nullable=False)
    vc_company_sname = Column(VARCHAR(256), nullable=False)
    vc_company_name = Column(VARCHAR(512))
    l_establish_date = Column(VARCHAR(50))
    l_company_type = Column(VARCHAR(50), nullable=False)
    vc_country_no = Column(VARCHAR(3))
    l_area_no = Column(VARCHAR(50))
    d_updatetime = Column(DateTime, nullable=False)
    l_first_date = Column(VARCHAR(50))
    l_update_date = Column(VARCHAR(50))
    vc_company_en_name = Column(VARCHAR(200))
    vc_company_en_sname = Column(VARCHAR(100))
    c_is_branch_company = Column(CHAR(1))
    vc_legal_representative = Column(VARCHAR(100))
    vc_chairman = Column(VARCHAR(100))
    vc_general_manager = Column(VARCHAR(100))
    vc_board_secretary = Column(VARCHAR(100))
    vc_bs_tel = Column(VARCHAR(50))
    vc_bs_fax = Column(VARCHAR(50))
    vc_bs_email = Column(VARCHAR(50))
    vc_bs_auth_represent = Column(VARCHAR(100))
    vc_secu_aff_represent = Column(VARCHAR(100))
    vc_sar_tel = Column(VARCHAR(50))
    vc_sar_fax = Column(VARCHAR(50))
    vc_sar_email = Column(VARCHAR(50))
    vc_inst_property = Column(VARCHAR(6))
    l_currency = Column(VARCHAR(50))
    en_reg_capital = Column(Float)
    vc_reg_address = Column(VARCHAR(200))
    vc_reg_postcode = Column(VARCHAR(20))
    vc_address = Column(VARCHAR(200))
    vc_postcode = Column(VARCHAR(20))
    vc_comp_tel = Column(VARCHAR(50))
    vc_fax = Column(VARCHAR(50))
    vc_email = Column(VARCHAR(100))
    vc_web = Column(VARCHAR(50))
    vc_serv_tel = Column(VARCHAR(50))
    vc_comp_evolut = Column(VARCHAR(2000))
    vc_bus_scope = Column(VARCHAR(2000))
    vc_main_bus = Column(VARCHAR(2000))
    l_reg_date = Column(VARCHAR(50))
    vc_license_no = Column(VARCHAR(50))
    vc_tax_reg_no = Column(VARCHAR(50))
    vc_local_tax_reg_no = Column(VARCHAR(50))
    vc_discloseinfo_web = Column(VARCHAR(200))
    vc_discloseinfo_newspaper = Column(VARCHAR(200))
    l_status = Column(VARCHAR(50))
    vc_inst_lvl = Column(VARCHAR(50))
    c_is_listed = Column(CHAR(1))
    en_auth_cap_stock = Column(NUMBER(19, 0, False))
    vc_inst_type = Column(VARCHAR(200))
    vc_serv_fax = Column(VARCHAR(50))
    l_employees_no = Column(VARCHAR(50))
    l_employees_no_date = Column(VARCHAR(8))
    l_bus_scale = Column(VARCHAR(50))
    vc_region2_name = Column(VARCHAR(128))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return   'vc_company_code'