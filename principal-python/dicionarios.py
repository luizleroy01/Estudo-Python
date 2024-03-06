# dictionaries are an data structure that contains a set of pair key and value 

pessoa = {"nome":"Luiz Eduardo","idade":22,"peso":80,"altura":1.62}

print("Informations about pessoa:")
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["peso"])
print(pessoa["altura"])

#method keys that return keys of dictionary
keys = list pessoa.keys()
print("Chaves do dicionario pessoa:", keys)

#method values that returns values of pair key value in dictionary
values = list pessoa.values()
print("Valores do dicionario pessoa:",values)

#method item tha return a set of tuples that contains a pair key value of dictionary on each position
items = list pessoa.items()
print("List de tuplas do dicionário:",items)