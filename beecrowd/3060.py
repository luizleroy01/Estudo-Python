import math

V = int(input())
P = int(input())

resto = V % P
parcelas = list()

# para arredondar para cima usa-se a função ceil
teto = math.ceil(float(V/P *1.0)) 
# para arredondar para baixo usa-se a função floor
chao = math.floor(float(V/P *1.0))

for i in range(0,P):
    if i < resto:
        parcelas.append(teto)
    else:
        parcelas.append(chao)

for parcela in parcelas:
    print(parcela)
