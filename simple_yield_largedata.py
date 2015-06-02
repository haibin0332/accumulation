##back up basic code template which is used for processing data with large volume
##use yield to return data in order to avoid memory usage

import csv

path1=r'C:\Users\mq42200466\Desktop\data_long.csv'

#with open(path, 'rb') as f:
#    f_csv = csv.reader(f)
#    headers = next(f_csv)

def read_file(path): 
  BLOCK_SIZE = 1024 
  with open(path, 'rb') as f: 
    while True: 
      block = f.read(BLOCK_SIZE) 
      if block: 
        yield block 
      else: 
        return      
#print (read_file(path1)) generator

temp=read_file(path1) 

###read per BLOCK_SIZE data    
print (next(temp))

####read all the data with generator
for i in temp:
  
      print i