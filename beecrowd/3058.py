
N = int(input())

i = 0
mercados = {}

while i<N:
    line = str(input())
    data = line.split(' ')
    P = float(data[0])
    G = int(data[1])

    aux = 1000  * P
    total = aux / G
    mercados[i+1] = total
    i+=1

minimo = mercados.get(1)
for mercado in mercados.values():
    if mercado < 0:
        minimo = mercado

print(format(minimo,".2f"))