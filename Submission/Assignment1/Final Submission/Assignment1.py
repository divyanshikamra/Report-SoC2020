from random import randint
import random
from numpy import diff
import numpy as np
import matplotlib.pyplot as plt

numofruns = 0
runs = []
sum = 0
totalit = []
p = 0
for i in range(100):

    a = [0] * 10000
    a[4999] = 1
    iterations = 0
    numofones = 0
    index = set([0])
    for i in range(10000):
        index.add(i)

    plot1x = []
    plot1y = []

    while (numofones != 10000):
        for x in range(10000):
            if a[x] == 1:
                c = randint(1, 100)
                if c <= 35:
                    a[abs(x - 1)] = 1
                d = randint(1, 100)
                if d <= 35:
                    a[(x + 1) % 10000] = 1

        anyten = random.sample(index, 10)
        for i in range(5):
            temp = a[anyten[i]]
            a[anyten[i]] = a[anyten[9 - i]]
            a[anyten[9 - i]] = temp

        iterations = iterations + 1
        numofones = 0

        for w in range(10000):
            if a[w] == 1:
                numofones = numofones + 1

        plot1x.append(iterations)
        plot1y.append(numofones)
    if p == 0:
        plt.plot(plot1x, plot1y)
        plt.show()
        dy = diff(plot1y)
        dx = diff(plot1x)
        dydx = [i / j for i, j in zip(dy, dx)]
        dydx.append(0)
        plt.figure()
        poly = np.polyfit(plot1x, dydx, 20)
        poly_y = np.poly1d(poly)(plot1x)

        plt.plot(plot1x, dydx, color='yellow')
        plt.plot(plot1x, poly_y, color='red')
        plt.show()

    numofruns = numofruns + 1
    p = 10
    sum=sum+iterations
    runs.append(numofruns)
    totalit.append(iterations)

avg = sum / 100
print('The average number of iterations for 100 runs are', avg)
plt.plot(runs, totalit)
plt.show()
