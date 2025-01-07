# for inside for loop:
#both inner and outer loops are executing completely?
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
# iterations
'''
iteration1:first outer loop is for  i in the range of (1,6),so i fetch the values till 5.
iteration2:next inner loop is for j in the range of (1,6), so j fetch the values till 5.
iteration3: it will print the i,j values, besides each together
'''
# breaking inner loop with inner loop value

'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
'''            
 # iterations
 iteration1: it will fetech i=1 in the oueter for loop and next it will fetch j=1 in the inner loop ,it checks the condition so 
               not satisfiedso it will print 11
  iteration2: it will fetech i=1 in the oueter for loop and next it will fetch j=2 in the inner loop ,it checks the condition so 
              not satisfiedso it will print 12
  iteration3: it will fetech i=3 in the oueter for loop and next it will fetch j=3 in the inner loop ,it checks the condition so 
               not satisfiedso it will print 13
  iteration4: it will fetech i=1 in the oueter for loop and next it will fetch j=4 in the inner loop ,it checks the condition so 
              it satisfied so it will break the loop
 iteration5: it will go to  fetch i=2 in the outer loop and next it will fetch j=1 in the inner loop ,it check the condition so not
             satisfied it will print 21  
 iteration6: it will go to  fetch i=2 in the outer loop and next it will fetch j=2 in the inner loop ,it check the condition so not
              satisfied it will print 22
 iteration7: it will go to  fetch i=2 in the outer loop and next it will fetch j=3 in the inner loop ,it check the condition so not
              satisfied it will print 23
 iteration8: it will go to  fetch i=2 in the outer loop and next it will fetch j=1 in the inner loop ,it check the condition so it is 
              satisfied it wil break the loop
 iteration9: it will go to  fetch i=3 in the outer loop and next it will fetch j=1 in the inner loop ,it check the condition so not
             satisfied it will print 31
 iteration10: it will go to  fetch i=3 in the outer loop and next it will fetch j=2 in the inner loop ,it check the condition so not
              satisfied it will print 32
 iteration11: it will go to  fetch i=3 in the outer loop and next it will fetch j=3 in the inner loop ,it check the condition so not
              satisfied it will print 33
 iteration12: it will go to  fetch i=3 in the outer loop and next it will fetch j=4 in the inner loop ,it check the condition so it is
               satisfied it will break the loop
 iteration13: it will go to  fetch i=4 in the outer loop and next it will fetch j=1 in the inner loop ,it check the condition so not
              satisfied it will print 41 so it will go to that range and checks the conditionns
 iteration14: it will go to  fetch i=5 in the outer loop and next it will fetch j=1 in the inner loop ,it check the condition so not
               satisfied it will print 51 so it will go to that range checks the conditions
# breaking outer loop with outer loop value
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if i==3:
        break
 #Iterations:
iteration1: it will fetch i=1 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          outer loop 1==3 false it wil print 11
 iteration2: it will fetch i=1 in the outer loop and next it will fetch j=2 in the inner loop,it checks the condition
              outer loop 1==3 false it wil print 12            
 iteration3: it will fetch i=1 in the outer loop and next it will fetch j=3 in the inner loop,it checks the condition
              outer loop 1==3 false it  print 13 and so it will fetch inner loop values upto 5 it print the values
 iteration4: it will fetch i=2 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
             outer loop 2==3 false it wil print 21 so it will fech inner loop values upto 5 it print the  values
 iteration5: it will fetch i=3 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
            outer loop 3==3 true it break the loop
 iteration6: it will fetch i=4 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
               outer loop 4==3 false it will print 41 and so it will fetch inner loop values upto 5 it print the values
 iteration7: it will fetch i=5 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
             outer loop 5==3 false it  print 51 and so it will fetch inner loop values upto 5 it print the values
#Breaking outer loop with outer loop value
for i in range(1,6):
    if i==3:
        break
    for j in range(1,6):
        print(i,j)
# iterations
Iteration1: it will fetch i=1 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          outer loop 1==3 false so it will the 11
Iteration2:it will fetch i=1 in the outer loop and next it will fetch j=2 in the inner loop,it checks the condition
          outer loop 1==3 false it wil print 12
Iteration3:it will fetch i=1 in the outer loop and next it will fetch j=3 in the inner loop,it checks the condition
          outer loop 1==3 false it wil print 13 and so it will print the values upto 5
Iteration4:it will fetch i=2 in the outer loop and next it will fetch j=2 in the inner loop,it checks the condition
          outer loop 2==3 false it wil print 21 and  so it will print the values upto 5         
Iteration5:it will fetch i=3 in the outer loop and next it will fetch j=2 in the inner loop,it checks the condition
          outer loop 3==3 satisfied it break the loop    

 # Breaking outer loop with inner loop value
''' for i in range(1,6):
     if j==3:
         break
     for j in range(1,6):
         print(i,j)
output:  Error becoz j is not defined
'''
#  Breaking outer loop with inner loop value
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    for j==3:
        break
# Iterations
'''
iteration1: it will fetch i=1 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 1==3 false it wil print 11 and so it will fetch inner loop values upto range so it will the print the values
iteration2: it will fetch i=2 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 2==3 false it wil print 21 and so on it will fetch inner loop values upto range so it will the print the values
iteration3: it will fetch i=3 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 3==3 true but it intially done opration upto 5 then it checks the condition
iteration4: it will fetch i=4 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 4==3 false it wil print 41 and  so it will fetch inner loop values upto range so it will the print the values          
iteration5: it will fetch i=5 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 5==3 false it wil print 41 and  so it will fetch inner loop values upto range so it will the print the values          

#  Breaking outer loop with inner loop value
'''for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    for j==3:
        break
# iterations:
'''
iteration1:it will fetch i=1 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 1==5 false it wil print 11 and so it will fetch inner loop values upto range so it will the print the values
iteration2:it will fetch i=2 in the outer loop and next it will fetch j=2 in the inner loop,it checks the condition
          inner loop 2==5 false it wil print 12 and so it will fetch inner loop values upto range so it will the print the values
iteration3:it will fetch i=3 in the outer loop and next it will fetch j=3 in the inner loop,it checks the condition
          inner loop 3==5 false it wil print 13 and so it will fetch inner loop values upto range so it will the print the values
iteration4:it will fetch i=4 in the outer loop and next it will fetch j=4 in the inner loop,it checks the condition
          inner loop 4==5 false it wil print 14 and so it will fetch inner loop values upto range so it will the print the values
iteration5:it will fetch i=5 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 5==5 false it wil print 11 and so it will fetch inner loop values upto range so it will the print the values
           so,loop will stop the termination becoz condition is sastisfied
'''           
# while inside while loop
i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j+=1
    i+=1    
iterations:
iteration1:it will fetch i=1 in the outer loop and next it will fetch j=1 in the inner loop,it checks the condition
          inner loop 1==3 after operation false it wil print 11 and so it will fetch inner loop values upto range so it will the print the values

               
