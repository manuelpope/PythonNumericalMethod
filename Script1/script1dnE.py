
# -------------------

j21 = 3.873502 * (10 ** -25)
j20 = 1.548478 * (10 ** -23)
result = []
result.append(j21)
result.append(j20)
itera = [item for item in range(1,20)]
itera.reverse()

for n in itera:
    ji = (((2 * n) - 4) * j21) - j20
    j21 = j20
    j20 = ji

    print("index" +str(n)+" : ",ji)
    result.append(ji)

