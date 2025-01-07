'''
a=int(input())
while a<10:
    print(a)
    a+=1
    '''
# wap to print the numbers b/w given number to 10 in a reverse order?
'''
n=int(input())
while n>10:
    print(n)
    n-=1
'''
#wap to print the squares of numbers in a given range ?
'''
ll=int(input())
ul=int(input())
i=ll
while i<ul:
    print(i**2)
    i+=1
'''
# wap to print 1 to 10 numbers ?
'''
a=int(input())
while a<11:
    print(a)
    a+=1
'''
# wap to print even numbers b/w 1 to 25?
'''
n=int(input())
while n<26:
    if n%2==0:
        print(n)
    n+=1    
'''
# wap to check given number is perfect or not?
'''
n=int(input())
dsum=0
i=1
while i<=n//2:
    if n%i==0:
        dsum+=1
    i+=1
if n==dsum:
    print(n,'is perfect')
else:
    print(n,'is not perfect')
    
'''













