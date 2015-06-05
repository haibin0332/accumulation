import re  
########################################### 
text = 'www.python.org'  
m = re.match(r'p', text)  
if m:  
    print 'yes' 
else:  
    print 'not match'  
 
#output: not match
#only do match operation at the begin of text
#so, if text = 'python.org', return yes
###########################################   
text = 'www.python.org'  
m = re.search(r'p', text)  
if m:  
    print 'yes'  
else:  
    print 'not search'  
#output 'yes' 
#searching match re
#############################################
text = 'a,b,c,d'
text1 = 'a,,,b,,c,d' 

print re.split(r'[,]+', text)
#output ['a', 'b', 'c', 'd']
print re.split(r'[,]+', text1)
#output ['a', 'b', 'c', 'd'] 
print re.split(r'[,]+', text1, maxsplit=1) #number to split  
#output ['a', 'b,,c,d']
print re.split(r'[,]+', text1, maxsplit=2)
#output ['a', 'b', 'c,d']
#############################################
#important function findall
pat=r'[a-zA-Z]+'
text='hmm...rr....."I said that",,,'

print re.findall(pat, text)
#output ['hmm', 'rr', 'I', 'said', 'that']
temp=re.findall(pat, text)
print len (temp) # 5
############################################## 
#replace pattern (oo) with -
text = "Good, he is cool."  
print re.sub(r'oo', '-', text) 
#output G-d, he is c-l.
emphasis_pat=r'\*([^\*]+)\*'
#<em>\1</em> is the important part makes re.sub different from replace function
#re.sub(pattern, repl, string/text) finding all the matched pattern in string and replace with repl
#在repl中以\n形式出现的任何转义序列都会被模式中与组n匹配的字符串替换掉
inputStr='hello 111 world 111'
replacedStr=inputStr.replace('111', '222')
print replacedStr

print re.sub(emphasis_pat, r'<em>\1</em>', 'hello, *world*!')
#finding pattern emphasis_pat, replace with r'<em>\1</em>'  \1 means group 1
#output hello, <em>world</em>!
#greedy
emphasis_pat=r'\*(.+)\*' 
print re.sub(emphasis_pat, r'<em>\1</em>', '*This* is *example*!')
#output <em>This* is *example</em>!
#non-greedy
emphasis_pat=r'\*(.+?)\*'
print re.sub(emphasis_pat, r'<em>\1</em>', '*This* is *example*!')
#output <em>This</em> is <em>example</em>!
###############################################
print re.escape(text) 
#output Good\,\ he\ is\ cool\. #divide special character
###############################################
#re
#.ython=python,jython,qython,etc
#python.org=python\.org
#[pj]ython=python,jython
#[0-9a-zA-Z]=any character
#[^abc]=any character other than a b c (opposite)
#r'(http://)?(www\.)?python\.org'='http://www.python.org', 'http://python.org', 'www.python.org','python.org' (option)
#(pat)* (0 or n); (pat)+ (1 or n); (pat){m,n} (m to n)
#r'^ht+p'=http://python.org, httttp://python.org  not www:http//python.org
###############################################
#group
#There (is a (bee)).
#group 0: There is a bee; group 1: is a bee; group 2: bee

#r'www\.(.+)\.com' group 1: all the res meet pattern (.+)
#get certain group that you are interested
m=re.match(r'www\.(.+)\.com', 'www.python.com')
print m.group(1) #get information of group 1 
#output python  if text is 'www.python.org' return error no pattern match
print m.start (1) #group 1 start index
print m.end (1) # group 1 end index
print m.span (1)
################################################

inputStr='hello 111 world 111'
replacedStr=inputStr.replace('111', '222')
print replacedStr
#it is difficult for replacing if inputStr = 'hello 123 world 456'
inputStr='hello 123 world 456'
replacedStr=re.sub('\d+', '222', inputStr)
print replacedStr
################################################

# 找到并把整个形如pattern的字符串用crifanli替换掉
inputStr = 'hello crifan, nihao adfg'
replacedStr = re.sub(r'hello (\w+), nihao', 'crifanli', inputStr);
print "replacedStr={}".format(replacedStr)
#output replacedStr=crifanli adfg

