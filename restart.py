'''s='pavan'
for i in s:
    print(i)
'''
'''l=[12,45,'hai',3.5,[17,34]]
for i in l:
    print(i)
          '''
'''s=('pavan',12,34,5.6,(23,45))
for i in s:
    print(i)
    '''
'''d={'name':'pavan','age':22}
for k,v in d.items():
    print(k,v)
'''
'''d={'name':'pavan','age':22}
for key in d:
    print(key,d[key])
'''
#wap to print how many elements are present in the given cdt?
'''cdt=eval(input("enter cdt"))
c=0
for i in cdt:
    c+=1
print(c)
'''
#wap to print how many times a substring present in the given string??
'''ms=input("enter the ms ")
ss=input("enter the ss")
c=0
for el in ms:
    if el==ss:
        c+=1
print(c)
'''
# wap to print how many numbers are present in the string?
'''s=input("enter the string")
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)        
'''
# wap to find the sum of digits present in the given string?
'''s=input("enter the string")
sum=0
for i in s:
  if i.isdigit():
      k=int(i)
      sum+=k
print(sum)      
'''
# wap to find the sum of even  digits present in the given string?
'''
s=input("enter the string")
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            sum+=k
print(sum)            
'''
'''
s=input("enter the string")
sum=0
for i in s:
    if i.isdigit() and int(i)%2==0:
        sum+=1
print(sum)
'''
n=int(input())
dsum=0
dummy=n
while n>0:
    rem=dummy%10
    dummy=dummy//10
    dsum+=rem
if n%dsum==0:
    print(n,"is harshad")
else:
    print(n,'is not harshad')
          







































