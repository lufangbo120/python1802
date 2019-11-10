import sqlacodegen
import subprocess
import os
# 需要手动修改
TABLENAME = 't_v_gp3_dimi_amoun'
# 输入路径
OUTDir = ''

tablenamelower = str(TABLENAME).lower()

scmd =r"sqlacodegen --tables {0}{5} --outfile {0}.py oracle+cx_oracle://{1}:{2}@{3}/{4}".format(tablenamelower,"md","md","10.88.158.97","hxtkdb",OUTDir)
#scmd = 'sqlacodegen --tables t_bsc_industrypartition --outfile t_bsc_industrypartition.py oracle+cx_oracle://md:md@10.88.158.97/hxtkdb'
print('开始生成文件，请稍等......')
#subprocess.run(scmd)
os.system(scmd)
