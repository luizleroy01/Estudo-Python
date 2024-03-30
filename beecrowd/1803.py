aux = []
matriz = []
i =0
tam = 0

while i < 4:
    linha = str(input())
    tam = len(linha)
    caracteres = list(linha)
    matriz.append(caracteres)
    i+=1

i =0 
j =0
strF = []
strL = []
num_caractres = tam - 2
codificada = {}
for i in range(0,num_caractres):
    chave = i+1
    codificada[chave] = []


i =0
j =0
while i < 4:
    while j < tam:
        if j == 0:
            strF.append(matriz[i][j])
        elif j == (tam-1):
            strL.append(matriz[i][j])
        else:
            codificada[j].append(matriz[i][j])
        j+=1
    j =0
    i+=1
num = []
F = int(''.join(str(n) for n in strF))
L = int(''.join(str(l) for l in strL))
for v in codificada.values():
    aux = ''.join(c for c in v)
    numero = int(aux)
    num.append(numero)

#convertendo os numeros em caracteres
palavra = ''
for n in num:
    c = ((F * n) +L )% 257 
    caracter = chr(c)
    palavra+=caracter

print(palavra)
