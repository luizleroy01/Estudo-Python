
N = int(input())

i = 0
mercados = {}

while i<N:
    line = str(input())
    data = line.split(' ')
    P = float(data[0])
    G = int(data[1])

    if G < 1000:
        aux = P * 1000
        aux2 = float(aux /G)
        total = aux2
    else:
        total = P

    mercados[i+1] = total
    i+=1

minimo = mercados.get(1)
for mercado in mercados.values():
    if mercado < minimo:
        minimo = mercado

print(format(minimo,".2f"))