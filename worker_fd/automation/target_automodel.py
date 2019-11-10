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

    # 需要手动修改
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
            logger.info( '{}加载常量有错误'.format(self.get_param('taskid')))
    def automodel_target(self):
        TABLENAME = self.target_table_name.replace(' ','')        #如果从数据库中取出来的数据后面有空格就删掉
        # 输入路径
        OUTDir = ''

        tablenamelower = str(TABLENAME).lower()

        scmd = "sqlacodegen --tables {0}{5} --outfile  model/{0}.py oracle+cx_oracle://{1}:{2}@{3}/{4}".format(tablenamelower,
                                                                                                      MD_SERVER_USER,
                                                                                                      MD_SERVER_PASS,
                                                                                                      MD_SERVER_ADDRESS,
                                                                                                      MD_SERVICE_NAME,
                                                                                                     OUTDir
                                                                                                      )
        logger.info('开始生成文件，请稍等......')

        try:
            os.system(scmd)
            sysstr = platform.system()
            if sysstr == "Linux":
                os.system("sed -i s/'NUMBER([0-9]*, [0-9]*, True)'/'VARCHAR(50)'/g  model/{0}.py".format(tablenamelower))
                os.system("sed -i s/'NUMBER(asdecimal=False)'/'VARCHAR(50)'/g  model/{}.py".format(tablenamelower))
                os.system("sed -i s/'NUMBER(scale=0, asdecimal=False)'/'VARCHAR(50)'/g  model/{}.py".format(tablenamelower))
            logger.info('生成文件成功，文件名为' + TABLENAME)
        except:
            logger.info('生成文件失败')
        with open('model/{}.py'.format(self.target_table_name), 'r', encoding='utf-8') as fw:
            a = fw.readlines()
        b = []
        for i in a:

            if 'vc_md5' not in i:
                if self.target_orm_name in i:
                    i = i.replace('{}'.format(self.target_orm_name),'{}'.format(self.source_orm_name),1)
                elif i == "    __tablename__ = '{}'\n".format(self.target_table_name):   #不能替换首字母防止表名不同
                    i =i.replace('{}'.format(self.target_table_name),'{}'.format(self.source_table_name),1)   #有多个t 不能直接替换,只替换1个
                b.append(i)
        with open('model/{}.py'.format(self.source_table_name), 'w', encoding='utf-8') as fw:
            fw.writelines(b)

    def func_str_target(self):
        df2 = pd.read_sql(
            "select c.column_name columnName,case when cu.column_name is null then 'false' else 'true' end as pkColumn from user_tab_columns c left join user_constraints au on c.table_name = au.table_name and au.constraint_type = 'P' left join user_cons_columns cu on cu.constraint_name = au.constraint_name and c.column_name = cu.column_name left join user_col_comments cmts on cmts.table_name = c.table_name and cmts.column_name = c.column_name where c.table_name = UPPER('{}') order by pkColumn desc".format(self.target_table_name),
            engine_target)        #区分哪些是主键
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
        with open('model/{}.py'.format(self.target_table_name), 'a+', encoding='utf-8') as fw:  # 打开文件
            fw.write('\n'"    "'def __str__(self):''\n' '        ''return''  ''{}'.format(list1))

    def func_str_source(self):
        df2 = pd.read_sql(
            "select c.column_name columnName,case when cu.column_name is null then 'false' else 'true' end as pkColumn from user_tab_columns c left join user_constraints au on c.table_name = au.table_name and au.constraint_type = 'P' left join user_cons_columns cu on cu.constraint_name = au.constraint_name and c.column_name = cu.column_name left join user_col_comments cmts on cmts.table_name = c.table_name and cmts.column_name = c.column_name where c.table_name = UPPER('{}') order by Pkcolumn desc".format(
                self.target_table_name),
            engine_target)  # 先排序不然不能判断前几个是key键
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
        with open('model/{}.py'.format(self.source_table_name), 'a+', encoding='utf-8') as fw:  # 打开文件
            fw.write('\n'"    "'def __str__(self):''\n' '        ''return''  ''{}'.format(list1))

    def run(self):
        if self.l_auto_model != 0:  # 等于0手动生成模型
            self.automodel_target()
            self.func_str_target()
            self.func_str_source()


regiest_task("TargetAutoModel", TargetAutoModel)