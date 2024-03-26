line = str(input())
aux = line.split(' ')
n = int(aux[0])
I = int(aux[1])
F = int(aux[2])

lineNumbers = str(input())
aux = lineNumbers.split(' ')
vet = []

for num in aux:
    vet.append(int(num))

pares = 0

i = 0
j = 0
lista = set()

while i < n:
    j = i+1
    while j < n:
        soma = vet[i] + vet[j]
        if soma >= I and soma <= F:
            pares+=1
        j += 1
    i += 1

print(pares)

