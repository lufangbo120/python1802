from pandas import DataFrame
from settings import logger
import pandas as pd

def dataframe_to_orm(orm, dataframe):
    field_name_list = orm.__mapper__.tables[0].columns._data._list
    tempdict1 = DataFrame(dataframe)[field_name_list]
    for field_name in field_name_list:
        try:
            stype = orm.__dict__.get(field_name).type.__visit_name__
            if stype == 'string':
                tempdict1[field_name] = tempdict1[field_name].astype(str)
                tempdict1[field_name].replace({'nan': None, 'None': None}, inplace=True)
            elif stype == 'text':
                tempdict1[field_name] = tempdict1[field_name].astype(str)
                tempdict1[field_name].replace({'nan': None, 'None': None}, inplace=True)
            elif stype == 'numeric':
                tempdict1[field_name] = tempdict1[field_name].astype(float)
                tempdict1[field_name] = tempdict1[field_name].where(tempdict1[field_name].notnull(), None)
            elif stype == 'datetime':
                tempdict1[field_name] = pd.to_datetime(tempdict1[field_name])
        except:
            logger.error('数据类型转换出错')
    df_dict = tempdict1.to_dict(orient='record')
    recordlist = []
    for r in df_dict:
        record = orm(**r)
        recordlist.append(record)
    return recordlist
