'''
n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars-=1
    spaces+=1
        
'''
'''
n=int(input())
stars=1
for i in range(1,n+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    stars+=1
'''
'''
n=int(input())
stars=1
spaces=n-1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    spaces-=1
    stars+=1
  '''
'''
n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for st in range(1,stars+1):
        print("*",end=" ")
    for sp in range(1,spaces+1):
        print(" ",end=" ")
    print()
    stars-=1
    spaces+=1
 '''
n=int(input())
stars=1
spaces=0
for row in range(1,n+1):
    for sp  in range(1,spaces+1):
        print(" ",end=" ")
    for st in range(1,stars+1):
        print("*",end=" ")
    print()
    spaces+=1
    










