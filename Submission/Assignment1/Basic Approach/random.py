from random import randint
import random
import matplotlib.pyplot as plt 

a=[0]*1000                              #making an array of 1000 elements all equal to 0
value=randint(100,900)                  #finding a random integer to assign it's coresponding value in array =1
a[value]=1

iterations=0                            
numofones=0
index= set([0])                        #forming a set which has all numbers from 0 to 999 to use later to find 2 random indices that must be swapped
for i in range (1000):
  index.add(i)

xaxis=[]
yaxis=[]  

while(numofones!=1000):
    #assigning 1s to neighbours
  for x in range (0,1000):
    if a[x]==1:
      if (randint(0,1)==0):
        a[abs(x-1)]=1
      else:
        a[(x+1)%1000]=1
    
  anytwo= random.sample(index,2)    #finding two indices that are to be swapped
  temp= a[anytwo[0]]                #swapping them
  a[anytwo[0]]=a[anytwo[1]]
  a[anytwo[1]]=temp

  iterations= iterations+1       
  numofones=0

  for w in range(0,1000):           #checking if we have reached our target to get all 1s in array
    if a[w]==1:
      numofones= numofones+1 
      
  xaxis.append(iterations)      
  yaxis.append(numofones)
  
# extracting required results
print(iterations)
plt.plot(xaxis,yaxis)
plt.show()
