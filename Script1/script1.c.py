import decimal
import math
import matplotlib.pyplot as plt


def countfractions(d :float):
    d = decimal.Decimal(d.__str__())
    return d.as_tuple().exponent
def makeListDecimalsPlaces(ld:list):
    listDecims=[]
    for i in ld:
        listDecims.append(countfractions(i))
    return listDecims
def calculateErDecimals(dp:int):
    dp=math.fabs(dp)
    return 0.5*10**(1-dp)


j1 = 0.7651976865
j2 = 0.4400505857
result = []
result.append(j1)
result.append(j2)
for n in range(3, 22):
    ji = (((2 * n) - 4) * j2) - j1
    j1 = j2
    j2 = ji
    print(n)
    result.append(ji)
listFractionsTuples = [math.modf(item) for item in result]
listFractions= []
for f in listFractionsTuples:
    #print(f)
    listFractions.append(f[0])

print(listFractions)
listD = makeListDecimalsPlaces(listFractions)
print("List of decimals places")
print(listD)

print("list of erros decimal places--- ")
errorlist=[calculateErDecimals(dp) for dp in listD]
print(errorlist)
plt.plot(errorlist)

plt.show()



