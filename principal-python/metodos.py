palavra = 'aaabbbuuuttaaauuppaajnhjaava'

print(palavra.count('a'))

nome = 'Luiz'
print(nome.find('i'))

print(palavra.replace('a','*'))

#codificar e decodificar em bytes uma string
print(nome.encode())

#use of strip andjoin with python

teste = '-------Luiz Eduardo---------'
print(teste.strip("-"))

print(nome.startswith("L"))

print("*".join(nome))