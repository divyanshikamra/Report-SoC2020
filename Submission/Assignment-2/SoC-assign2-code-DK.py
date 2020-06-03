from random import randint
import random
from numpy import diff
import numpy as np
import matplotlib.pyplot as plt

numofruns=0
runs=[]
sum=0
totalit=[]
p=0

for i in range (500):
  a=[[0 for i in range(150)] for j in range(100)]
  b=[[0 for i in range(150)] for j in range(100)]
  a[50][75]=1
  iterations=0
  numofones=0

  plot1x=[]
  plot1y=[]

  while(numofones!=15000):
    list1=[]
    while(len(list1)!=8):
      a1= randint(0,99)
      b1= randint(0,149)
      if [a1,b1] not in list1:
        list1.append([a1,b1])
    list2=[]
    while(len(list2)!=8):
      c1=randint(0,99)
      d1=randint(0,149)
      if [c1,d1] not in list1 and [c1,d1] not in list2:
        list2.append([c1,d1])

    for x in range (8):
      temp=a[(list1[x][0])][(list1[x][1])]
      a[(list1[x][0])][(list1[x][1])]=a[(list2[x][0])][(list2[x][1])]
      a[(list2[x][0])][(list2[x][1])]=temp

    for i in range (100):
      for j in range (150):
        if a[i][j]==1:
          for u in range (i-1,i+2):
            for v in range (j-1,j+2):
              if u>=0 and v>=0:
                u=u%100
                v=v%150
                if random.random() <= 0.25:
                  b[u][v]=1

          for u in range (i-2,i+3):
            for v in range (j-2,j+3):
              if u>=0 and v>=0 and (u==i or u==i+2 or v==j or v==j+2):
                u=u%100
                v=v%150
                if random.random() <= 0.08 :
                  b[u][v]=1

    for i in range (100):
            for j in range (150):
              if b[i][j]==1:
                a[i][j]=1

    numofones=0
    iterations+=1
    for i in a:
      for j in i:
        if j==1:
          numofones=numofones+1
    plot1x.append(iterations)
    plot1y.append(numofones)
  if p==0:
    plt.plot(plot1x, plot1y)
    plt.show()
    dy = diff(plot1y)
    dx = diff(plot1x)
    dydx = [i / j for i, j in zip(dy, dx)]
    dydx.append(0)
    plt.figure()
    poly = np.polyfit(plot1x, dydx, 20)
    poly_y = np.poly1d(poly)(plot1x)

    plt.plot(plot1x, dydx, color='black')
    plt.plot(plot1x, poly_y, color='red')
    plt.show()

    numofruns = numofruns + 1
    p = 10
    sum=sum+iterations
    runs.append(numofruns)
    totalit.append(iterations)

avg = sum / 500
print('The average number of iterations for 500 runs are', avg)
plt.plot(runs, totalit)
plt.show()
