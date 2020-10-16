import math

import numpy as np
import decimal

def calculateError(listXi:list):

    listVecXi=[list(np.transpose(item)[0]) for item in listXi]
    erroList=[]
    xref=np.array([0.5,0.75,0.25,0.5])
    xref=np.transpose(xref)
    N= len(listVecXi)
    for x in range(1,(N)):
        ei= np.abs(np.array(listVecXi[x])-xref)
        er= min(ei)
        es= np.float64(0.5*10**-8)
        erroList.append(ei)
        if er <= es:
            return (x)

# initialize the matrix
D = np.array([[4, 0, 0, 0],
              [0, 4, 0, 0],
              [0, 0, 4, 0],
              [0, 0, 0, 4]])
# initialize the RHS vector
b = np.array([[1, 2, 0, 1]])
b = np.transpose(b)

#print(D)
#print(b)
Dinv = np.linalg.inv(D)
R = np.float64(np.array([[0, -1., -1., 0],
             [-1., 0, 0, -1.],
             [-1., 0, 0, -1.],
             [0., -1., -1., 0]]))
mDinv= Dinv.dot(-1)
print("-D matrix:: ")
print(mDinv)
T = np.dot(mDinv, R)
print(T)
C= Dinv.dot(b)
print(C)
x0=np.array([(0*10**16),(0*10**16),(0*10**16),(0*10**16)]).reshape(4,1)
x0=np.float64(x0)
listResultsxi=[]
for i in range(0,50):
    xi= (T.dot(x0))+C
    print(i,xi)
    listResultsxi.append(np.float64(xi))
    x0=xi
print(calculateError(listResultsxi))



