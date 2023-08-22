#código dedicado ao cálculo do imc em python

nome = str(input("Digite seu nome \n"))
peso = float(input("Digite seu peso\n"))
altura = float(input("Digite sua altura \n"))

def calculoIMC(peso,altura):
    #operador de potenciação (**)
    return (peso/(altura ** 2))

result = calculoIMC(peso,altura)

estado_imc = ""

if result < 18.5 :
    estado_imc = "Abaixo do peso"
elif result > 18.5 and result < 25:
    estado_imc = "Peso ideal"
elif result > 25 and result < 29.9:
    estado_imc = "Acima do peso"
else:
    estado_imc = "Obsesidade"

resposta = f'{nome} tem {altura:.2f} de altura, pesa {peso:.2f} e seu IMC é {result:.2f} de estado {estado_imc}'
print(resposta)