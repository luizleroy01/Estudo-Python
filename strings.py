#arquivo dedicado a manipulação de strings com python

print ("Hello World")

nome = "Luiz Eduardo"

outro_nome = f'{nome[:3]} Cruzeiro {nome[4:]}'

print(outro_nome)

#para contar quantas vezes uma letra ou palavra aperece em uma 
#frase, basta utilizar a função count em python

#no caso abaixo a letra que repete mais vezes é b
string = "aaaaaabbbbbbbcccdd"
qtd = 0
letra = ''
i =0
qtd = string.count(string[0])
while i < len(string):
    
    if string.count(string[i]) > qtd:
        qtd = string.count(string[i])
        letra = string[i]

    i+=1

print(f'A letra que aparece mais vezes é {letra} com {qtd} repetições') 