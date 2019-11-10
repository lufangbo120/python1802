from cerberus import Validator

from TopSpeedData_Worker.connection.oracle import connect_target, engine_target
import pandas as pd

class CustomValidator(Validator):

    def __init__(self,rule,target_table_name):#传不定长参数
        super(CustomValidator, self).__init__(rule)
        self.conn_target = connect_target()
        self.target_table_name = target_table_name
        self.tmp_data = pd.read_sql("select * from {}".format(self.target_table_name),con = engine_target)


    def _validate_isduplication(self, isduplication, field, value):#判断一个字段是否有重复值
        """ Test the oddity of a value.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        tmp_data = self.tmp_data[(self.tmp_data['{}'.format(field)] == '{}'.format(value))]
        if tmp_data.count()[0] == 2 and isduplication == True:
            self._error(field, "证券简称为{}的债券重复".format(tmp_data.values[0][0]))



# rule = {'vc_sname': {'isduplication': True}}
# v = CustomValidator(rule, 't_tmp_bsc_investment_advice')
# print(v.validate({'vc_sname': '银河次级'}))
# print(v.errors)


# schema = {'amount': {'odd': True, 'type': 'integer'}}
# v = MyValidator(schema)
# v.validate({'amount': 10})
#print(v.errors)
#v.validate({'amount': 9})
#print(v.errors)
