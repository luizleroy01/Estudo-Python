#este código é dedicado a implementação dos trechos de condicionais em python

num = int(input("Digite um numero\n"))

if num % 2 == 0 :
    print("O numero é par")
elif num % 2 != 0:
    print("o numero é impar")


#definir função através do número

role = int(input("Digite o numero da função \n"))

if role == 1:
    print("Programador")
elif role == 2 :
    print("Administrador")
else:
    print("Engenheiro")