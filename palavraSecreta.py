#exercício palavra secreta em python
palavra = "agua"
tentativas = 5
secret = "*" * len(palavra)

print("Bem vindo!!!, Este é o jogo Palavra Secreta")
print(f'palavra: {secret}')
print(f'Você tem {tentativas} tentativas')
encontrou = False
while tentativas >= 0:
    letra = str(input("Digite uma letra:\n"))
    i =0
    res = ''
    
    while i < len(secret):
        
        if(secret[i] == "*"):
            if letra == palavra[i]:
                res += f'{palavra[i]}'
                encontrou = True
            else:
                res += "*"
        else:
            res+= f'{secret[i]}'
        i+=1
    
    secret = res
    print(f'palavra: {secret}')
    
    if(not encontrou):
        tentativas -= 1
    print(f'Você ainda tem {tentativas} tentativas')
    
    if(secret == palavra):
        break

    encontrou = False
    

if(tentativas >= 0):
    print("Você venceu :)!!!")
else:
    print("Você perdeu :(")

print("Fim de jogo!!!!")