# coding: utf-8
from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class VdiEtlInstructionDetail(Base):
    __tablename__ = 'vdi_etl_instruction_detail'

    key_etl_instruction = Column(VARCHAR(50), primary_key=True)
    id_ind_port_code = Column(VARCHAR(30))
    id_ins_data_bgndate = Column(DateTime)
    id_ins_data_enddate = Column(DateTime)
    id_ins_data_kind = Column(VARCHAR(50))
    id_ins_exec_date = Column(DateTime)
    id_ins_exec_groupno = Column(VARCHAR(50))
    ins_exec_update_style = Column(VARCHAR(50))
    ins_exec_rec_source = Column(VARCHAR(50))
    ins_exec_bgntime = Column(DateTime)
    ins_exec_endtime = Column(DateTime)
    ins_exec_state = Column(VARCHAR(50))
    ins_rec_time = Column(DateTime)
    ins_remark = Column(VARCHAR(200))
    src_port_code = Column(VARCHAR(60))
    ind_rec_time = Column(DateTime)
    vc_source = Column(VARCHAR(20))
    vc_update_operater = Column(VARCHAR(20))
    d_updatetime = Column(DateTime)

    def __str__(self):
        return   'key_etl_instruction'