#exercicio beecrowd 1278
import re
N = int(input())
frases = []
result = []
i = 0
while i < N:
    aux = str(input())
    frases.append(aux)
    i+=1

maior = 0
for frase in frases:
    f = frase.strip()
    #utilizando o modulo re para operações utilizando regex
    f = re.sub(r'\s+',' ',f)
    tam = len(f)
    if tam > maior:
        maior = tam
    result.append(f)


for frase in result:
    print(frase.rjust(maior))
