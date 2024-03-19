#More of methods with python
pessoa = {
    'nome': 'Luiz Eduardo ',
    'sobrenome': 'Leroy Souza'
}
# Define a default value to a key not defined
pessoa.setdefault('idade',0)

for key,value in pessoa.items():
    print(f"{key} : {value}")

# Use of deep and shalow copy

d1 = {'a':1, 'b':2, 'c':3, 'd':4}

#deep copy with d1 = d2 and shalow copy with d1.copy()
d2 = d1.copy()
d2['a'] = 'luiz'

for valor in d1.values():
    print(valor)

pessoa.update({
    'altura':1.60
})

for key,value in pessoa.items():
    print(f"{key} : {value}")

tupla = ('role','programador')

tupla = ('role', 'programador')
pessoa[tupla[0]] = tupla[1]

for key,value in pessoa.items():
    print(f"{key} : {value}")