#código dedicado ao exercício para validação de cpf
#Coletar a soma dos primeiros 9 dígitos do cpf multiplicando
#cada algarismo por uma conatagem regressiva começando de 10

# Somar todos os resultados e multiplicar por 10

#obter o resto da divisão por 11

#se o resultado do resto for maior que 9, o valor do décimo
# dígito é 0, senão é o valor do próprio resto

#Para o décimo primeiro dígito coleta a soma dos 10 primeiros
#dígitos do cpf multiplicando cada algarismo por uma conatgem regressiva
#começando de 11,  os outros passos são semelhantes ao anterior
#teste : '829.089.400-78'
cpf = str(input("Digite seu cpf:\n"))

cpf.replace('.','').replace('-','')
digi_cpf = []
soma_cpf = 0
contagem_digito_1 = 10
contagem_digito_2 = 11
digito_10 = 0
digito_11 = 0

# para o dígito 10
for i in range(len(cpf)):
    if(cpf[i] != '.' and cpf[i] != '-'):
        digi_cpf.append(int(cpf[i]))
        
print(*digi_cpf,end="\n")


for i in range(len(digi_cpf)- 2):
    digito = digi_cpf[i]
    soma_cpf += (digito * contagem_digito_1)
    contagem_digito_1 -= 1

print(soma_cpf,end="\n")

resultado = soma_cpf * 10
resto_11 = resultado % 11

if resto_11 <= 9:
    digito_10 = resto_11
else:
    digito_10 = 0

print("Digito 10 :",digito_10)

# para o dígito 11

soma_cpf = 0

for i in range(len(digi_cpf)- 1):
    digito = digi_cpf[i]
    soma_cpf += (digito * contagem_digito_1)
    contagem_digito_2 -= 1

print(soma_cpf,end="\n")

resultado = soma_cpf * 10
resto_11 = resultado % 11

if resto_11 <= 9:
    digito_11 = resto_11
else:
    digito_11 = 0

print("Digito 11 :",digito_11)

tamanho = len(digi_cpf)
verificaCPF = digi_cpf[tamanho-2] == digito_10 and digi_cpf[tamanho -1] == digito_11

if(verificaCPF):
    print("CPF válido")
else:
    print("CPF inválido")