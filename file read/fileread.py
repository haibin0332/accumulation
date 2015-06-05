# -*- coding: utf-8 -*-
def read_file_data(filepath):
    '''
    @param filepath: read file path
    @return: list of data with \t
    '''
    fin = open(filepath, 'r')
    for line in fin:
        try:
# a=[1,2,3]
# a[:-1]=[1,2]; a[:]=[1,2,3]          
            line = line[:-1]
            if not line: continue
        except:
            continue       
        try:
            fields = line.split("\t")
        except:
            continue
        
        yield fields
    fin.close()

g=read_file_data(r'C:\Users\mq42200466\workspace\pyproj\template.txt')

for fields in g:  

  print fields
#output: ['[import time]']
#['Dear [name],']
#['I would like to learn how to program. I hear you use the [language] language a lot --']
#['And, by the way, is [email] your correct email address?']
#['thanks, [time.asctime()']
############################################################

def transform_list_to_dict(para_list):
        """把['a', 'b']转换成{'a':0, 'b':1}的形式
  @param para_list: 列表，里面是每个列对应的字段名
  @return: 字典，里面是字段名和位置的映射
        """
        res_dict = {}
        idx = 0
        while idx < len(para_list):
              res_dict[str(para_list[idx]).strip()] = idx
              idx += 1
        return res_dict

para_list=['a', 'b']

print transform_list_to_dict(para_list)
#output {'a': 0, 'b': 1}
###################################################################
