# -*- encoding:utf8 -*-
'''
Created on 2015��6��4��
'''
class FileUtil(object):
    '''general method for file/path operation
    '''
    @staticmethod
    def read_file_data(filepath):
        '''
    @param filepath: read file path
    @return: list of data with \t
        '''
        fin = open(filepath, 'r')
        for line in fin:
            try:
                line = line[:-1]
                if not line: continue
            except:
                continue            
            try:
                fields = line.split("\t")
            except:
                continue
            # �׳���ǰ�еķָ��б�
            yield fields
        fin.close()
    
    @staticmethod
    def transform_list_to_dict(para_list):
        """transfer ['a', 'b'] to {'a':0, 'b':1}
        @param para_list: 
        @return: dict, 
        """
        res_dict = {}
        idx = 0
        while idx < len(para_list):
            res_dict[str(para_list[idx]).strip()] = idx
            idx += 1
        return res_dict
    
