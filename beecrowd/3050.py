N = int(input())
linePredios = str(input())
aux = linePredios.split(" ")

predios = []

for predio in aux:
    predios.append(int(predio))

maxDist = 0
#primeiro encontrar a maior distancia entre o primeiro prédio e qualquer outro predio (target)
#Depois encontrar a maior distancia entre esse prédio (target) e qualquer outro prédio presente no conjunto

maxDist = 0
distancia1 =0
target = -1

#Maior distancia entre o primriro prédio e qualquer outro prédio target
for i in range(0,N):
    dist = predios[0] + i + predios[i]
    if dist > distancia1:
        distancia1 = dist
        target = i

#Maior distancia entre o prédio(target) e qualquer outro presente no conjunto
for i in range(0,N):
    if i != target:
        maxDist = max(maxDist,predios[target] + abs(target - i) + predios[i])


print(maxDist)
