from email import message
from re import M
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[1, 0], [0, 1]])
print(matrix2)
print(np.add(matrix1, matrix2))
print(np.divide(matrix1, matrix2))
#print(np.multiply(matrix1, matrix2))
print(np.dot(matrix1, matrix2))
print(np.sum(matrix1))
print(np.sum(matrix1, axis = 0))
print(np.sum(matrix1, axis = 1))
print("test print format: ", matrix1)
print(f"test print format: \n", matrix1)
print(f"The transpose of matrix1 is: \n", matrix1.T)   # here matrix1.T is the transpose of matrix1
#print(f"This is the inverse of matrix1: \n", matrix1)
print(np.transpose(matrix1))
print(np.invert(matrix1))           # the invert in numpy is used to computer bit-wise inversion of an array element wise
print(np.invert(0))                 # and a positive number x being inverted, the result is -x-1
print(np.invert(-1))
print(np.linalg.inv(matrix1))
 

person = input("what is your name\n")
message = "hello, {0}".format(person)
print(message)





























