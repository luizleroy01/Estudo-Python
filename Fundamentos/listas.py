#em python tremos as listas que também funcionam como arrays
#Suporta vários valores de qualquer tipo
#métodos uteis: append, insert, del, clear,extend, pop...
nome = 'Luiz'
lista = []
for i in range(0,len(nome)):
    lista.append(nome[i])

print(lista," de tamanho ",len(lista))

numeros = [1,2,3,4,5]

#insere na lista
numeros.append(6)
print(numeros)

del numeros[2]
print(numeros)

#excluir elemento do final
numeros.pop()
print(numeros)

#adiciona em um indice específico insert(indice,valor)
numeros.insert(0,50)
print(numeros)

#concatenar listas
letras = ['a','b','c']
numeros.extend(letras)
print(numeros)

for i in range(len(numeros)):
    print(numeros.index(numeros[i]))

#empacotamento e de desempacotamento
#desempacota a lista nomes, o primriro índice é atribuído á variavel nome
#o restante da lista nomes é empacotado em resto
nomes = ['Luiz','Eduardo','Leroy']
nome,*resto = nomes
print(nome,resto)

#limpa a lista
numeros.clear()

#simulando uma matriz com listas dentro de listas
matriz = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()
