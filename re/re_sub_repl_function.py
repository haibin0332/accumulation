import re

def pythonReSubDemo():
    """
        demo Pyton re.sub
    """
    inputStr = "hello 123 world 456"
    
    def _add111(matched):
        #intStr = matched.group(0) 
        intStr = matched.group(0) # the same with matched.group(1)
        intValue = int(intStr)
        addedValue = intValue + 111 
        addedValueStr = str(addedValue)
        return addedValueStr
#(?p=name)        


    #replacedStr = re.sub("\d+", _add111, inputStr)
    replacedStr = re.sub(r'(\d+)', _add111, inputStr)
#   if  "hello 123 world 456 I am 789"   
#   replacedStr = re.sub(r'(\d+)', _add111, inputStr, 2) #hello 234 world 567 I am 789, which only deals with first 2 matched pattern    
#     print re.match(r'(\d+)', inputStr) #none (match only work for the beginning of text)
#     print re.search(r'(\d+)', inputStr).group() #123
#     print re.search(r'(\d+)$', inputStr).group() #456
    print "replacedStr=",replacedStr #hello 234 world 567

###############################################################################
if __name__=="__main__":
    pythonReSubDemo()
    
 
# inputStr = "hello crifan, nihao abdgg";
# replacedStr = re.sub(r"hello (\w+), nihao", "\g<1>", inputStr); #\g<1> group 1
# print "replacedStr=",replacedStr; #crifan  
# #output replacedStr= crifan abdgg
