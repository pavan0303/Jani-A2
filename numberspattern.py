# pattern number1

n=int(input())
spaces=0
stars=n
dummy=1
for row in range(1,n+1):
    for sp in range(1,row+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        
        

    print()
    spaces+=1
    stars-=1
    dummy+=1
  
# number pattern 2
'''
n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    stars+=1
    dummy+=1
'''
# number pattern 3

n=int(input())
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,row+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    stars+=1
    spaces-=1
    dummy+=1
    
 # number pattern 4
'''
n=int(input())
spaces=0
stars=1
dummy=1n
for row in range(1,n+1):
     for sp in range(1,row+1):
         print(' ',end=' ')
     for st in range(1,stars+1):
         print(dummy,end=' ')
     print()
     spaces+=1
     dummy+=1
  '''

# pattern program
'''
n=int(input())
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
     for sp in range(1,row+1):
         print(' ',end=' ')
     for st in range(1,stars+1):
         print(dummy,end=' ')
     print()
     spaces-=1
     dummy+=1
'''
#pattern program
'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
  '''
# pattern program
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
    '''
# pattern program
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
    print()
    dummy+=1
 '''
 #pattern program
'''
n=int(input())
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    stars+=2
    spaces-=1
    dummy+=1
'''
# pattern program
'''
n=int(input())
spaces=n//2
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
        
    print()
    if row<=n//2:
        stars+=2
        spaces-=1
    else:
        stars-=2
        spaces+=1
    dummy+=1       
'''
# pattern2 program
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(dummy,end=' ')
        dummy+=1
    print()        
  '''
# pattern2 program

n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,row+1):
        if row==col:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
            dummy+=1
    print()
    
# pattern2 ptogram
'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,row+1):
        if row+col==n+1:
            print(dummy,end=' ')
        else:
            print(' ',end=' ')
            dummy+=1
    print()
'''









              
