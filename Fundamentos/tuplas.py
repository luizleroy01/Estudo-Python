#tuplas são um tipo de dado que correspondem auma lista imutável
nomes = 'joao','carlos','matheus'

print(nomes)

#listas enumeradas com enumerate
#enumerate cria tuplas com o índice e o valor
for index,nome in enumerate(nomes):
    print(index,nome)