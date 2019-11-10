# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TTmpBscInvestmentAdvice(Base):
    __tablename__ = 't_tmp_bsc_investment_advice'

    vc_sname = Column(VARCHAR(200), primary_key=True)
    l_issue_date = Column(VARCHAR(200))
    vc_issuer_name = Column(VARCHAR(200))
    vc_guarantor = Column(VARCHAR(200))
    en_issue_amount = Column(VARCHAR(200))
    vc_duration = Column(VARCHAR(200))
    vc_uwrtname = Column(VARCHAR(2000))
    vc_creditrate = Column(VARCHAR(200))
    vc_ratecomname = Column(VARCHAR(200))
    vc_inner_creditrate = Column(VARCHAR(200))
    vc_rate_operator = Column(VARCHAR(200))
    vc_industry_name = Column(VARCHAR(200))
    vc_interest_interval = Column(VARCHAR(4000))
    vc_market_rate = Column(VARCHAR(200))
    vc_star_level = Column(VARCHAR(200))
    vc_advice_type = Column(VARCHAR(200))
    vc_advice_rate = Column(VARCHAR(200))
    vc_investment_advice = Column(VARCHAR(4000))
    vc_referral = Column(VARCHAR(200))
    vc_floor_price = Column(VARCHAR(200))
    b_in_bondpool = Column(VARCHAR(200))
    b_holiday = Column(VARCHAR(200))
    vc_bond_type = Column(VARCHAR(200))
    vc_market = Column(VARCHAR(200))
    b_pledged = Column(VARCHAR(200))
    d_bid_begintime = Column(VARCHAR(200))
    d_bid_endtime = Column(VARCHAR(200))
    vc_fundamental = Column(VARCHAR(4000))
    vc_primary_rating = Column(VARCHAR(200))
    l_date = Column(NUMBER(20, 8, True))
