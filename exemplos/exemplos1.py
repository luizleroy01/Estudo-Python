#exercicios para prática da lógica com python

try:
    num = int(input("Digite um numero:\n"))
    if num % 2 == 0:
        print("O numero é par\n")
    else:
        print("O numero é impar\n")
except:
    print("O numero que voce digitou não é inteiro\n")


#exercício 2
print("Horas do dia")
try:
    hora = int(input("Digite uma hora do dia:\n"))

    if hora > 0 and hora <= 11:
        print("Bom dia!!!\n")
    elif hora > 11 and hora <= 18:
        print("Boa tarde!!!\n")
    elif hora > 18 and hora < 24:
        print("Boa noite\n")

except:
    print("O valor digitado não corresponde a um numero\n")

#exercício 3

nome = str(input("Digite seu nome"))
tamanho = len(nome)
if tamanho <= 4 :
    print("Seu nome é pequeno")
elif tamanho > 4 and tamanho <= 6 :
    print("Seu nome é normal")
else:
    print("Seu nome é grande")