# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, VARCHAR, text
from sqlalchemy.dialects.oracle.base import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TLogDqc(Base):
    __tablename__ = 't_log_dqc'

    l_serial_no = Column(NUMBER(asdecimal=False), primary_key=True)
    vc_target_table = Column(VARCHAR(64))
    c_module = Column(CHAR(1))
    l_level = Column(NUMBER(scale=0, asdecimal=False))
    l_kind = Column(NUMBER(scale=0, asdecimal=False))
    vc_msg = Column(VARCHAR(4000))
    c_deal_flag = Column(CHAR(1))
    vc_query_sql = Column(VARCHAR(4000))
    d_updatetime = Column(DateTime, server_default=text("sysDATE"))
    l_date = Column(NUMBER(8, 0, False))
    vc_col_code = Column(VARCHAR(32))
    l_dict_id = Column(NUMBER(scale=0, asdecimal=False))
    vc_err_code = Column(VARCHAR(64))
    vc_memo = Column(VARCHAR(1000))
    vc_second_class_name = Column(VARCHAR(240))
    vc_workflow_name = Column(VARCHAR(240))
    vc_workflow_name_cn = Column(VARCHAR(240))
    l_workflow_runid = Column(NUMBER(scale=0, asdecimal=False))
    l_tabrule_id = Column(NUMBER(scale=0, asdecimal=False))
    c_mail_flag = Column(CHAR(1))
    l_task_id = Column(NUMBER(scale=0, asdecimal=False))
    l_object_id = Column(NUMBER(scale=0, asdecimal=False))
