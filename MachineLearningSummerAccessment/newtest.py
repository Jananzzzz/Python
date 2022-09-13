import numpy as np
import pandas as pd  #pandas is widely used in data analysis and machine learning
import pylab              # ploting library and math extension

def compute_error(b, w, data):         # compute the error/loss
    totalError = 0;
    x = data['楼层']
    y = data['房屋价格（万元/平方米）']
    totalError = (y - w*x - b)**2
    totalError = np.sum(totalError, axis = 0)       # axis = 0 means row by row
    return totalError/float(len(data))             # len(data) the length of the data sheet

def optimizer(data, starting_b, starting_w, learning_rate, num_iter):
    b = starting_b
    w = starting_w
    # gradient descent
    for i in range(num_iter):
        b, w = compute_gradient(b, w, data, learning_rate)
        if i%100 == 0:
            print('iter times: {0} error: {1}'.format(i, compute_error(b, w, data )))
    return [b,w]

def compute_gradient(b_current, w_current, data, learning_rate):
    b_gradient = 0
    w_gradient = 0
    N = float(len(data))
    x = data['楼层']
    y = data['房屋价格（万元/平方米）']
    b_gradient = -(2/N)*(y - w_current*x - b_current)
    w_gradient = -(2/N)*x*(y - w_current*x - b_current)
    # check here to see if b is a sheet
    b_gradient = np.sum(b_gradient, axis = 0)
    w_gradient = np.sum(w_gradient, axis = 0)
    new_b = b_current - (learning_rate * b_gradient)
    new_w = w_current - (learning_rate * w_gradient)
    return [new_b,  new_w]

def plot_data(data, b, w):
    x = data[('楼层')]
    y = data['房屋价格（万元/平方米）']
    y_predict = w*x + b
    pylab.plot(x, y, 'o')
    pylab.plot(x, y_predict, 'k-')
    pylab.show()
    # read the official documention of pylab


def Linear_regression():
    data = pd.read_excel('data.xlsx')      # pd.read_excel('data_xlsx) import data
    # steps to initiate a classifier:  
    # define hyperparameters: y = wx + b
    # define the learn rate
    # define the number of iterations
    learning_rate = 0.016
    initial_b = 0.0
    initial_w = 0.0
    num_iter = 10000
    print('Initial Parameter:\n initial_b = {0} \n initial_w = {1} \n error of begin = {2}\n'.format(initial_b, initial_w, compute_error(initial_b, initial_w, data)))    
    [b, w] = optimizer(data, initial_b, initial_w, learning_rate, num_iter)
    print('Final Parameter:\n b = {0}\n w = {1}\n error or end = {2}' .format(b, w, compute_error(b, w, data))) 
    plot_data(data, b, w)

if __name__ == '__main__':
    Linear_regression()
   



# read the official documention of pandas
# always a : behind a function 
# def fuction(parameter):























