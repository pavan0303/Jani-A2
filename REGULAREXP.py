'''
import re
s='hai python'
print(re.match('h',s))


import re
s='hai python'
'''
'''
#print(re.match('\w{3}',s))
print(re.match('p',s))
print(re.match('a',s))
print(re.search('a',s))
print(re.search(' ',s))
print(re.search('th',s))
print(re.search('hai',s))
print(re.search("hai python",s))
print(re.search('w',s))
print(re.findall('python',s))
print(re.findall('werr',s))
print(re.findall('h',s))
print(re.findall('th',s))
print(re.findall('ht',s))
print(re.findall(" ",s))
print(re.findall('ph',s))
print(re.findall('etij',s))
print(re.finditer('h',s))
io=re.finditer('h',s)
for i in io:
    print(i)
    
'''
'''
print(re.findall('E',s))
print(re.findall('123',s))
print(re.findall('@#',s))
print(re.findall('.',s))
print(re.findall('^h',s))
print(re.findall('' '$',s))
print(re.findall('2$',s))
'''
import re
s="hai heeep hep hp heep hellpo heap"
print(re.findall('he*',s))
print(re.findall('e*',s))














                    




