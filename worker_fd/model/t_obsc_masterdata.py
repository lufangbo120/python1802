# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, LargeBinary, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TObscMasterdatum(Base):
    __tablename__ = 't_obsc_masterdata'

    recordid = Column(VARCHAR(50), primary_key=True)
    amt_issued = Column(VARCHAR(50))
    amt_outstanding = Column(VARCHAR(50))
    assumed_idx = Column(VARCHAR(50))
    basic_spread = Column(VARCHAR(50))
    bb_composite = Column(VARCHAR(10))
    calc_typ_des = Column(VARCHAR(18))
    callable = Column(CHAR(4))
    cntry_issue_iso = Column(CHAR(4))
    cntry_of_risk = Column(CHAR(4))
    cnvx_mid = Column(VARCHAR(50))
    convertible = Column(CHAR(4))
    cpn = Column(VARCHAR(50))
    cpn_cap = Column(VARCHAR(50))
    cpn_crncy = Column(VARCHAR(8))
    cpn_floor = Column(VARCHAR(50))
    cpn_freq = Column(VARCHAR(50))
    cpn_typ = Column(VARCHAR(24))
    crncy = Column(VARCHAR(8))
    cur_mkt_cap = Column(VARCHAR(50))
    cv_cnvs_px = Column(VARCHAR(50))
    cv_cnvs_ratio = Column(VARCHAR(50))
    cv_common_ticker_exch = Column(VARCHAR(18))
    cv_start_dt = Column(DateTime)
    cv_until = Column(DateTime)
    days_to_nxt_refix_tdy = Column(VARCHAR(50))
    days_to_settle = Column(VARCHAR(50))
    day_cnt_des = Column(VARCHAR(22))
    default_date = Column(DateTime)
    delivery_typ = Column(VARCHAR(30))
    dual_crncy = Column(VARCHAR(8))
    dur_adj_mid = Column(VARCHAR(50))
    dur_mid = Column(VARCHAR(50))
    dvd_crncy = Column(VARCHAR(8))
    dvd_ex_dt = Column(DateTime)
    dvd_sh_12m = Column(VARCHAR(50))
    eqy_beta = Column(VARCHAR(50))
    eqy_dvd_ex_flag = Column(CHAR(4))
    eqy_init_po_dt = Column(DateTime)
    eqy_init_po_sh_px = Column(VARCHAR(50))
    eqy_sh_out_tot_mult_sh = Column(VARCHAR(50))
    erisa = Column(CHAR(4))
    exch_code = Column(VARCHAR(18))
    ffiec_test = Column(VARCHAR(8))
    first_cpn_dt = Column(DateTime)
    fixed = Column(CHAR(4))
    flt_bench_multiplier = Column(VARCHAR(50))
    flt_cpn_convention = Column(VARCHAR(30))
    flt_days_prior = Column(VARCHAR(50))
    flt_min_cpn = Column(VARCHAR(50))
    flt_pay_day = Column(VARCHAR(30))
    fund_comp_name = Column(VARCHAR(512))
    fund_guarantor = Column(VARCHAR(30))
    fund_incept_dt = Column(DateTime)
    futures_category = Column(VARCHAR(30))
    fut_cont_size = Column(VARCHAR(50))
    gics_sector = Column(VARCHAR(50))
    gics_group_num = Column(VARCHAR(50))
    govt_eqv_yld_mid = Column(VARCHAR(50))
    guarantors_list = Column(LargeBinary)
    id_bb = Column(VARCHAR(9))
    id_bb_company = Column(VARCHAR(50))
    id_bb_global = Column(VARCHAR(12))
    id_bb_ultimate_parent_co = Column(VARCHAR(50))
    id_cusip = Column(VARCHAR(9))
    id_hong_kong_cmu = Column(VARCHAR(11))
    id_isin = Column(VARCHAR(12))
    id_mdm_misc_domes = Column(VARCHAR(19))
    id_sedol1 = Column(VARCHAR(7))
    id_stock_exchange = Column(VARCHAR(14))
    id_valoren = Column(VARCHAR(12))
    industry_group = Column(VARCHAR(24))
    industry_sector = Column(VARCHAR(24))
    industry_subgroup = Column(VARCHAR(30))
    insurance_status = Column(CHAR(4))
    int_acc = Column(VARCHAR(50))
    issuer = Column(VARCHAR(512))
    issue_dt = Column(DateTime)
    issue_px = Column(VARCHAR(50))
    is_eps = Column(VARCHAR(50))
    is_reg_s = Column(CHAR(4))
    is_unit_traded = Column(CHAR(4))
    last_update = Column(DateTime)
    linear_accrual_interest = Column(CHAR(4))
    lower_tier2_capital = Column(CHAR(4))
    market_issue = Column(VARCHAR(25))
    maturity = Column(DateTime)
    mid_px_val_bp = Column(VARCHAR(50))
    most_recent_reported_factor = Column(VARCHAR(50))
    mtg_amort_typ = Column(VARCHAR(8))
    mtg_collat_dt = Column(DateTime)
    mtg_cred_enhanc = Column(LargeBinary)
    mtg_factor_num_dt = Column(DateTime)
    mtg_final_pay_dt = Column(DateTime)
    mtg_hist_prepay_life = Column(LargeBinary)
    mtg_life_cap = Column(VARCHAR(50))
    mtg_life_floor = Column(VARCHAR(50))
    mtg_ltv_histogram = Column(LargeBinary)
    mtg_pay_delay = Column(VARCHAR(8))
    mtg_pool_number = Column(VARCHAR(8))
    mtg_prepay_model = Column(VARCHAR(8))
    mtg_prepay_speed = Column(VARCHAR(50))
    mtg_typ = Column(VARCHAR(8))
    mtg_wacpn = Column(VARCHAR(50))
    mtg_wac_histogram = Column(LargeBinary)
    mtg_wal = Column(VARCHAR(50))
    mtg_wam = Column(VARCHAR(50))
    mtg_wam_histogram = Column(LargeBinary)
    name = Column(VARCHAR(512))
    nav_crncy = Column(VARCHAR(8))
    nxt_call_dt = Column(DateTime)
    nxt_cpn_dt = Column(DateTime)
    nxt_premium_call_px = Column(VARCHAR(50))
    nxt_put_dt = Column(DateTime)
    nxt_put_px = Column(VARCHAR(50))
    nxt_refix_dt = Column(DateTime)
    nxt_sink_amt = Column(VARCHAR(50))
    nxt_sink_dt = Column(DateTime)
    oas_spread_mid = Column(VARCHAR(50))
    opt_put_call = Column(VARCHAR(8))
    par_amt = Column(VARCHAR(50))
    penultimate_cpn_dt = Column(DateTime)
    pe_ratio = Column(VARCHAR(50))
    prev_cpn_dt = Column(DateTime)
    pricing_source = Column(VARCHAR(30))
    prvt_place = Column(CHAR(4))
    putable = Column(CHAR(4))
    put_days_notice = Column(VARCHAR(50))
    px_dirty_clean = Column(VARCHAR(5))
    px_last = Column(VARCHAR(50))
    px_round_lot_size = Column(VARCHAR(50))
    recovery_lag = Column(VARCHAR(50))
    redemp_val = Column(VARCHAR(50))
    refix_freq = Column(VARCHAR(50))
    regulatory_typ = Column(VARCHAR(16))
    reset_idx = Column(VARCHAR(15))
    rtg_fitch = Column(VARCHAR(16))
    rtg_moody = Column(VARCHAR(16))
    rtg_sp = Column(VARCHAR(16))
    security_des = Column(VARCHAR(30))
    security_short_des = Column(VARCHAR(30))
    security_typ = Column(VARCHAR(28))
    short_name = Column(VARCHAR(512))
    sinkable = Column(CHAR(4))
    structured_note = Column(CHAR(4))
    ticker_and_exch_code = Column(VARCHAR(12))
    tier1_capital = Column(CHAR(4))
    trade_crncy = Column(VARCHAR(8))
    upper_tier2_capital = Column(CHAR(4))
    voting_rights = Column(VARCHAR(50))
    wrt_crncy = Column(VARCHAR(8))
    wrt_delta_last = Column(VARCHAR(50))
    wrt_divisor = Column(VARCHAR(50))
    wrt_exer_dt = Column(DateTime)
    wrt_exer_px = Column(VARCHAR(50))
    wrt_exer_typ = Column(VARCHAR(8))
    wrt_expire_dt = Column(DateTime)
    wrt_issue_amt = Column(VARCHAR(50))
    wrt_issue_dt = Column(DateTime)
    wrt_issue_prc = Column(VARCHAR(50))
    wrt_outstanding = Column(VARCHAR(50))
    wrt_put_or_call = Column(VARCHAR(8))
    wrt_settle_typ = Column(VARCHAR(13))
    wrt_undl_ticker = Column(VARCHAR(16))
    yas_bnchmrk_bond = Column(VARCHAR(15))
    yas_curve_id = Column(VARCHAR(6))
    yld_ytm_mid = Column(VARCHAR(50))
    tier2_capital_non_specific = Column(CHAR(4))
    id_bb_unique = Column(VARCHAR(30))
    quote_typ = Column(VARCHAR(50))
    market_sector = Column(VARCHAR(50))
    name_chinese_simplified = Column(VARCHAR(512))
    d_updatetime = Column(DateTime)
    eqy_prim_exch = Column(VARCHAR(12))
    eqy_prim_exch_shrt = Column(VARCHAR(8))
    issuer_cmpid = Column(VARCHAR(8))
    country_risk_iso_code = Column(VARCHAR(4))
    min_piece = Column(VARCHAR(50))
    prpl = Column(VARCHAR(4))
    wrt_undl_unique_id = Column(VARCHAR(30))
    undl_id_bb_unique = Column(VARCHAR(30))
    country_iso = Column(VARCHAR(4))
    cntry_of_domicile = Column(VARCHAR(4))
    mty_typ = Column(VARCHAR(18))
    cdr_settle_code = Column(VARCHAR(4))
    is_unsecured = Column(VARCHAR(4))
    int_acc_dt = Column(DateTime)
    fut_val_pt = Column(VARCHAR(50))
    last_tradeable_dt = Column(DateTime)
    cntry_of_incorporation = Column(VARCHAR(128))
    fund_typ = Column(VARCHAR(128))
    fund_asset_class_focus = Column(VARCHAR(128))
    regulator_structure = Column(VARCHAR(128))
    industry_group_num = Column(VARCHAR(50))
    industry_sector_num = Column(VARCHAR(50))
    industry_subgroup_num = Column(VARCHAR(50))
    issuer_industry = Column(VARCHAR(64))
    type_of_bond = Column(VARCHAR(64))
    market_sector_des = Column(VARCHAR(32))
    security_typ2 = Column(VARCHAR(28))
    market_status = Column(VARCHAR(32))
    start_acc_dt = Column(DateTime)
    is_perpetual = Column(VARCHAR(2))
    c_as_bond_or_equity = Column(CHAR(1))
    gics_sector_name = Column(VARCHAR(30))
    gics_industry_group = Column(VARCHAR(50))
    gics_industry_group_name = Column(VARCHAR(30))
    gics_industry = Column(VARCHAR(50))
    gics_industry_name = Column(VARCHAR(30))
    gics_sub_industry = Column(VARCHAR(50))
    gics_sub_industry_name = Column(VARCHAR(30))
    eqy_fund_crncy = Column(VARCHAR(5))
    is_cd = Column(VARCHAR(1))
    fd_initial_val = Column(VARCHAR(50))
    eqy_sh_out = Column(VARCHAR(50))
    vc_md5 = Column(VARCHAR(32))
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))

    def __str__(self):
        return  str(self.recordid)+'$*'+str(self.vc_md5)