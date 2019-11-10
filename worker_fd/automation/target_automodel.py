# coding=gbk
import os
import platform

import sqlacodegen
import subprocess

from TopSpeedData_Worker.connection import connect_mysql
from settings import MD_SERVER_USER, MD_SERVER_PASS, \
    MD_SERVER_ADDRESS, MD_SERVICE_NAME
from TopSpeedData_Worker.tkacmbase.taskbase import TkTaskBase, regiest_task

import pandas as pd
from TopSpeedData_Worker.connection.oracle import engine_target
from settings import logger

class TargetAutoModel(TkTaskBase):
    parameterkeys = ["taskid"]
    # parametertype = [int]

    def __init__(self, param):
        TkTaskBase.__init__(self, param)
        self.conn_mysql = connect_mysql()

        self.target_orm_name = None
        self.source_orm_name = None

        self.target_table_name = None
        self.source_table_name = None
        self.l_auto_model = None

        self.load_target_table_name()

    # ��Ҫ�ֶ��޸�
    def load_target_table_name(self):
        try:
            self.target_orm_name = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(self.get_param('taskid')))[0][2]
            self.source_orm_name = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(self.get_param('taskid')))[0][1]
            self.target_table_name = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(self.get_param('taskid')))[0][4]
            self.source_table_name = self.conn_mysql.execute('select * from t_extract_config where l_task_id = {}'.format(self.get_param('taskid')))[0][3]
            self.l_auto_model = self.conn_mysql.execute(
                'select * from t_extract_config where l_task_id = {}'.format(self.get_param('taskid')))[0][10]

            self.conn_mysql.close()

        except:
            logger.info( '{}���س����д���'.format(self.get_param('taskid')))
    def automodel_target(self):
        TABLENAME = self.target_table_name.replace(' ','')        #��������ݿ���ȡ���������ݺ����пո��ɾ��
        # ����·��
        OUTDir = ''

        tablenamelower = str(TABLENAME).lower()

        scmd = "sqlacodegen --tables {0}{5} --outfile  model/{0}.py oracle+cx_oracle://{1}:{2}@{3}/{4}".format(tablenamelower,
                                                                                                      MD_SERVER_USER,
                                                                                                      MD_SERVER_PASS,
                                                                                                      MD_SERVER_ADDRESS,
                                                                                                      MD_SERVICE_NAME,
                                                                                                     OUTDir
                                                                                                      )
        logger.info('��ʼ�����ļ������Ե�......')

        try:
            os.system(scmd)
            sysstr = platform.system()
            if sysstr == "Linux":
                os.system("sed -i s/'NUMBER([0-9]*, [0-9]*, True)'/'VARCHAR(50)'/g  model/{0}.py".format(tablenamelower))
                os.system("sed -i s/'NUMBER(asdecimal=False)'/'VARCHAR(50)'/g  model/{}.py".format(tablenamelower))
                os.system("sed -i s/'NUMBER(scale=0, asdecimal=False)'/'VARCHAR(50)'/g  model/{}.py".format(tablenamelower))
            logger.info('�����ļ��ɹ����ļ���Ϊ' + TABLENAME)
        except:
            logger.info('�����ļ�ʧ��')
        with open('model/{}.py'.format(self.target_table_name), 'r', encoding='utf-8') as fw:
            a = fw.readlines()
        b = []
        for i in a:

            if 'vc_md5' not in i:
                if self.target_orm_name in i:
                    i = i.replace('{}'.format(self.target_orm_name),'{}'.format(self.source_orm_name),1)
                elif i == "    __tablename__ = '{}'\n".format(self.target_table_name):   #�����滻����ĸ��ֹ������ͬ
                    i =i.replace('{}'.format(self.target_table_name),'{}'.format(self.source_table_name),1)   #�ж��t ����ֱ���滻,ֻ�滻1��
                b.append(i)
        with open('model/{}.py'.format(self.source_table_name), 'w', encoding='utf-8') as fw:
            fw.writelines(b)

    def func_str_target(self):
        df2 = pd.read_sql(
            "select c.column_name columnName,case when cu.column_name is null then 'false' else 'true' end as pkColumn from user_tab_columns c left join user_constraints au on c.table_name = au.table_name and au.constraint_type = 'P' left join user_cons_columns cu on cu.constraint_name = au.constraint_name and c.column_name = cu.column_name left join user_col_comments cmts on cmts.table_name = c.table_name and cmts.column_name = c.column_name where c.table_name = UPPER('{}') order by pkColumn desc".format(self.target_table_name),
            engine_target)        #������Щ������
        list2 = df2['columnname'].values
        is_key = df2['pkcolumn'].values
        keys = 0
        for i in is_key:
            if i == 'true':
                keys += 1
        list = []
        for i in list2:
            list.append(i)
        list.insert(keys, '$*')
        list = list[0:keys+1]
        list.append('vc_md5')
        list1 = ''
        for i in list:
            i = i.lower()
            if i == '$*':
                list1 += "'" + i + "'"
                list1 += "+"
            else:
                a = 'str(self.' + i + ')'
                list1 += a
                if i != list[-1]:
                    list1 += "+"
        with open('model/{}.py'.format(self.target_table_name), 'a+', encoding='utf-8') as fw:  # ���ļ�
            fw.write('\n'"    "'def __str__(self):''\n' '        ''return''  ''{}'.format(list1))

    def func_str_source(self):
        df2 = pd.read_sql(
            "select c.column_name columnName,case when cu.column_name is null then 'false' else 'true' end as pkColumn from user_tab_columns c left join user_constraints au on c.table_name = au.table_name and au.constraint_type = 'P' left join user_cons_columns cu on cu.constraint_name = au.constraint_name and c.column_name = cu.column_name left join user_col_comments cmts on cmts.table_name = c.table_name and cmts.column_name = c.column_name where c.table_name = UPPER('{}') order by Pkcolumn desc".format(
                self.target_table_name),
            engine_target)  # ������Ȼ�����ж�ǰ������key��
        list2 = df2['columnname'].values
        is_key = df2['pkcolumn'].values
        keys = 0
        for i in is_key:
            if i == 'true':
                keys += 1
        list = []
        for i in list2:
            list.append(i)
        list = list[0:keys ]
        list1 = ''
        for i in list:
            i = i.lower()
            if i.upper() != list[-1]:
                list1 +=" '{}'".format(i)
                list1 += "+'$*'+"
            else:
                list1 += " '{}'".format(i)
        with open('model/{}.py'.format(self.source_table_name), 'a+', encoding='utf-8') as fw:  # ���ļ�
            fw.write('\n'"    "'def __str__(self):''\n' '        ''return''  ''{}'.format(list1))

    def run(self):
        if self.l_auto_model != 0:  # ����0�ֶ�����ģ��
            self.automodel_target()
            self.func_str_target()
            self.func_str_source()


regiest_task("TargetAutoModel", TargetAutoModel)