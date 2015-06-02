#-*- coding: UTF-8 -*- 
import random
 
def get_data():
    """generate 3 random values within 0 to 9"""
    return random.sample(range(10), 3)
 

def consume():
    """display the running average of 'get_data'"""
    running_sum = 0
    data_items_seen = 0
  
    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
#.format in python
#the same as %s but new function is like 
#Input '{},{}'.format('a', 'b'); Output 'a, b' 
#Input '{1},{0}'.format('a', 'b'); Output 'a, b' 
#Input '{1},{0},{1}'.format('a', 'b'); Output 'b, a, b'  
#Input '{name},{age}'.format('age=a', 'name=b'); Output 'b, a'
#class Person:  
#    def __init__(self,name,age):  
#        self.name,self.age = name,age  
#        def __str__(self):  
#            return 'This guy is {self.name},is {self.age} old'.format(self=self)
#In: str(Person('a',b))  __str__ is called when the str function is applied to an object
#Out: 'This guy is a,is b old'
#
#In: '{:.2f}'.format(321.33345)
#Out: '321.33'
#In: '{:b}'.format(17)
#Out: '10001'
#In: '{:d}'.format(17)
#Out: '17'
#In: '{:o}'.format(17)
#Out: '21'
#In: '{:x}'.format(17)
#Out: '11'  
#In: '{:,}'.format(1234567890)
#Out: '1,234,567,890'   
        print('The running average is {}'.format(running_sum / float(data_items_seen)))
  
def produce(consumer):
    """generate or get data, and then sent to consumer"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield
  
if __name__ == '__main__':
    consumer = consume() #assign a generator
    consumer.send(None) #run the generator to first yield
    producer = produce(consumer)
  
    for _ in xrange(10):
        print('Producing...')
        next(producer) #run the generator 

      
def double_inputs():
  while True:
    x = yield
    yield x * 2
#############################################
gen = double_inputs()
gen.next() #run up to the first yield (x=yield) generator.next(), run the generator once
print gen.send(10) #goes into 'x' variable (to next yield x*2 20)

gen.next() #run up to the next yield (x=yield)
print gen.send(6) #goes into 'x' again (x*2)
   
        
