#codigo dedicado ao uso de excessoes compython
str = input("Digite um numero")
try:
    print(str)
    num = int(str)
    print(f'O numero é {num}')
except:
    print("Não é um numero")

#uso do none e not none

flag = None

condicao = True

if condicao:
    flag = True

if flag is None :
    print("Is None")

if flag is not None:
    print("Not none")


