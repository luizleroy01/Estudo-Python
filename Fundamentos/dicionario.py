#use of dictionaries with python
# Creating a dictionary
student = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'GPA': 3.5
}

# Accessing values using keys
print("Name:", student['name'])
print("Age:", student['age'])
print("Major:", student['major'])
print("GPA:", student['GPA'])

# Adding a new key-value pair
student['email'] = 'john.doe@example.com'

# Modifying a value
student['GPA'] = 3.7

# Removing a key-value pair
del student['age']

# Iterating over keys
print("Keys:")
for key in student.keys():
    print(key)

# Iterating over values
print("Values:")
for value in student.values():
    print(value)

# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# An example of dictionary for a people
pessoa = {
    'nome':'Luiz Eduardo',
    'sobrenome': 'Leroy Souza'
}

if pessoa.get('idade'):
    print('A chave existe')
else:
    print('A chave não existe')
    pessoa['idade'] = 22

for chave,valor in pessoa.items():
    print(chave,valor)

numeros = {'pares': [],
            'impares':[]
        }
num = int(input('Digite um numero'))

while num != 0:
    if num % 2 == 0:
        numeros['pares'].append(num)
    else:
        numeros['impares'].append(num)
    num = int(input('Digite um numero'))

listaNumeros = numeros.get('pares')
for item in listaNumeros:
    print(item,end=" ")