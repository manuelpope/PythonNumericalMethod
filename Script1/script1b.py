j1 = 0.7651976865
j2 = 0.4400505857
result = []
result.append(j1)
result.append(j2)
for n in range(3, 22):
    ji = (((2 * n) - 4) * j2) - j1
    j1 = j2
    j2 = ji
    index= "index: "+str(n)+" : "
    print(index,ji)
    result.append(ji)

