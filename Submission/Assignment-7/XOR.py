import numpy as np
import matplotlib.pyplot as plt

#taking inputs of XOR gate as training data
X_train=np.array([[0,0],[0,1],[1,0],[1,1]])
# .T is to take transpose of the matrix
y_train=np.array([0,1,1,0]).T
y_train=y_train.reshape(4,1)

turns=[]
errors_1=[]
errors_2=[]
errors_3=[]
errors_4=[]

def func(x):
    return 1/(1+np.exp(-x))

def derivative(t):
     return t*(1-t)

def train(lr=0.5,epochs=10000):
    #initialize
    inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2,2,1
    #Random weights and bias initialization
    hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
    hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
    output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
    output_bias = np.random.uniform(size=(1,outputLayerNeurons))

    for i in range(epochs):
        turns.append(i)
        #FORWARD PROPAGATION
        hidden_layer_activation = np.dot(X_train,hidden_weights)
        hidden_layer_activation += hidden_bias
        hidden_layer_output = func(hidden_layer_activation)

        output_layer_activation = np.dot(hidden_layer_output,output_weights)
        output_layer_activation += output_bias
        predicted_output = func(output_layer_activation)

        #Backpropagation
        error = y_train - predicted_output
        d_predicted_output = error *derivative(predicted_output)

        error_hidden_layer = d_predicted_output.dot(output_weights.T)
        d_hidden_layer = error_hidden_layer * derivative(hidden_layer_output)
        
        errors_1.append(error[0])
        errors_2.append(error[1])
        errors_3.append(error[2])
        errors_4.append(error[3])


        #Updating Weights and Biases
        output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
        output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
        hidden_weights += X_train.T.dot(d_hidden_layer) * lr
        hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr
    print(predicted_output)   
    return hidden_weights, hidden_bias,output_weights,output_bias

train(0.5,10000)
plt.plot(turns,errors_1,color="RED")
plt.plot(turns,errors_2,color="BLUE")
plt.plot(turns,errors_3,color="GREEN")
plt.plot(turns,errors_4,color="YELLOW")

plt.xlabel("Iterations")
plt.ylabel("Errors in hidden layer")
plt.title("WITH LEARNING RATE=0.5")
plt.show()
