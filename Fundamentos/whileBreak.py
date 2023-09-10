#código dedicado a prática das estruturas while e do comando break e continue

controle = 0 

while controle < 10 :
    if controle % 2 == 0:
        controle += 1
        continue

    print(controle)
    controle += 1
    if controle == 5:
        break

print("Fim do código")


#imprimindo valores de 1 a 9 em forma de matriz

LINHAS = 3
COLUNAS = 3

lin = 1
value = 1

while lin <= LINHAS:
    
    value1 = value + 1
    value2 = value + 2
    print(value,value1,value2)
    value = value2 + 1

    lin += 1
else:
    #em python temos exclusivamente o else juntamente do while
    print("Fim do loop")