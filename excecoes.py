#codigo dedicado ao uso de excessoes compython
str = input("Digite um numero")
try:
    print(str)
    num = int(str)
    print(f'O numero é {num}')
except:
    print("Não é um numero")
