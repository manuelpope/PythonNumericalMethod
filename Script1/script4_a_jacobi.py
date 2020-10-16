import numpy as np

ITERATION_LIMIT = 4

# initialize the matrix
D = np.array([[4, 0, 0, 0],
              [0, 4, 0, 0],
              [0, 0, 4, 0],
              [0, 0, 0, 4]])
# initialize the RHS vector
b = np.array([[1, 2, 0, 1]])
b = np.transpose (b)

print(D)
print(b)
Dinv = np.linalg.inv(D)
R = np.array([[0, -1., -1., 0],
             [-1., 0, 0, -1.],
             [-1., 0, 0, -1.],
             [0., -1., -1., 0]])
mDinv= Dinv.dot(-1)
print("-D matrix:: ")
print(mDinv)
T = np.dot(mDinv, R)
print("MatrixT",T)
C= Dinv.dot(b)
print(C)
x0=np.array([0,0,0,0]).reshape(4,1)
xi= (T.dot(x0))+C
print("Jacobi Result for "+ str(np.reshape(x0,(1,4))))
xi= np.transpose(xi)
print("xi::  ",xi)