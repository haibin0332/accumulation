####################################################
#1)random functions
####################################################
import random
 
#generate a float within 0 to 1
print random.random() 
 
#generate a float within [10, 20]
print random.uniform(10, 20)  
print random.uniform(20, 10)  
 
#generate a int within [12, 20]
print random.randint(12, 20)
 
 
#generate a int within range [10, 12, 14, 16,...98]
print random.randrange(10, 100, 2)
 
#select a element within string, list, tuple, etc
print random.choice("Python")   
print random.choice(["JGood", "is", "a", "handsome", "boy"])  
print random.choice(("Tuple", "List", "Dict"))  
 
 
#disorder a list
p = ["Python", "is", "powerful", "simple", "and so on..."]  
random.shuffle(p)  
print p  
 
 
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#select 5 elements from list  
slice = random.sample(list, 5)  
print slice  
#nothing change with the list
print list
##################################################
#2)lambda example 1
##################################################
#each element in a as the input for map function f
a=[1,2,3]
f=lambda x: x+1
print map(f, a)
#or
#lambda itself it a anonymous function (can be considered as lambda function with x as a parameter)
print (map (lambda x: x+1, [1,2,3]))
#or no lambda
a=[1,2,3]
r=[]
for each in a:
  r.append(each+1)
print r  
output: [2,3,4]
#####################################################
#3)lambad example 2
#####################################################
print map (lambda x: x*x, [y for y in range(10)]) 
#or
def sq(x):
    return x * x
print map(sq, [y for y in range(10)])
output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#####################################################
#4)re to obtain all .py files
#####################################################
##os.getcwd() ('C:\\Python27')
import os, re 
#f=lambda x: x+1 compare these two lambda functions
#two parameters dir and p as input for lambda function
f1 = lambda dir = os.getcwd(), p = '': [file for file in os.listdir(dir) if p == '' or re.search(p, file)] 
#dir = os.getcwd()
#p = ''
#[file for file in os.listdir(dir) if p == '' or re.search(p, file)]
#output:['DLLs', 'Doc', 'include', 'Lib', 'libs', 'LICENSE.txt', 'NEWS.txt', 'python.exe', 'pythonw.exe', 'README.txt', 'tcl', 'test', 'Tools', 'w9xpopen.exe']  
print f1(p = r'.py')  
#output:all .py files
#####################################################
#5)string or list reverse
#####################################################
s = 'abcd'  
print s[::-1]  
#output dcba
l = [1, 2, 3, 4]  
print l[::-1]
#output [4,3,2,1]
range(4)[::-1]
#output [3, 2, 1, 0] 
