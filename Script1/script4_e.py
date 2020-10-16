
import numpy as np
import decimal

def calculateError(listXi:list):

    listVecXi=[list(np.transpose(item)[0]) for item in listXi]
    erroList=[]
    N= len(listVecXi)
    for x in range(1,(N)):
        ei= np.array(listVecXi[x])-np.array(listVecXi[x-1])
        er= np.linalg.norm(ei)
        es= np.float64(0.5*10**-14)
        erroList.append(ei)
        if er <= es:
            result=[np.linalg.norm(item) for item in erroList]
            return (x,result)

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



