#re temple
import fileinput, re
#create re expression; match with content in () 
field_pat=re.compile(r'\[(.+?)\]')
############
#scope={'name' : 'Magnus Lie Hetland', 'email' : 'magnus@foo.bar', 'language' : 'python'}
scope={}
lines=[]
for line in fileinput.input('para.txt'):
#    line=tuple(line)
    line=line[:-1]
    line=eval(line) # change str "[('name', 'Magnus Lie Hetland')]" to [('name', 'Magnus Lie Hetland')] (strip "")  
    temp_line=line[0] 
    lines.append(temp_line)
scope=dict(lines)   
# text=''.join(lines)
#################
##
#m = re.match(r'(\d+)\.(\d*)', '3.14sss') 
#print m.group(0,1,2)
#output ('3.14', '3', '14')
def replacement (match):
  code = match.group(1) #get group 1
  try:
#g={'a':6}
#eval ("a+1", g)
#output 7    
    return str(eval(code, scope))
  except SyntaxError:
# (exec in) example exec is not a function
# g={'a':6, 'b':8}
#exec "global a; print a, b" in g
#output 6 8   
#exec (expr, globals)= exec expr in globals
#exec (expr, globals, locals)=exec expr in globals, locals
    exec code in scope
    return ''
################## 
#read the text 
lines=[]
for line in fileinput.input('template.txt'):
  lines.append(line)
text=''.join(lines)
##or
#text=''
#for line in fileinput.input():
#text+=line
##################
#replace and print
print field_pat.sub(replacement, text)

