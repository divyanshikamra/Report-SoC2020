import numpy as np
import matplotlib.pyplot as plt

X_train = np.array([[1,0,1],[0,0,1],[1,1,0],[1,1,1]])
y_train = np.array([[1,0,1,1]]).T
outputs1=[]
outputs2=[]
outputs3=[]
outputs4=[]

turns=[]

def func(x):
  return 1/(1+np.exp(-x))

def derivative(t):
  return t*(1-t)

def training_model(X_train,y_train,learning_rate=0.2,num_of_times=2000):
  np.random.seed(5)
  w=np.random.random((3,1))
  for i in range(num_of_times):
    predicted_output=func(np.dot(X_train,w))
    outputs1.append(predicted_output[0])
    outputs2.append(predicted_output[1])
    outputs3.append(predicted_output[2])
    outputs4.append(predicted_output[3])
    turns.append(i+1)
    error= (y_train-predicted_output)*derivative(predicted_output)
    w+= learning_rate*(np.dot(X_train.T,error))
  return w

x1=int(input())
x2=int(input())
x3=int(input())

if x1 in range(2) and x2 in range(2) and x3 in range(2):
  w1 = training_model(X_train, y_train)
  x_test = np.array([x1, x2, x3])
  prediction= func(np.dot(x_test,w1))
  print(prediction)
  if(prediction < 0.5):
    print("0")
  else:
    print("1")
else:
  print("Only 1 and 0 are allowed as entries")

plt.plot(turns,outputs1)
plt.plot(turns,outputs2)
plt.plot(turns,outputs3)
plt.plot(turns,outputs4)
plt.xlabel("Number Of Iterations")
plt.ylabel("Predicted_output")
plt.show()
