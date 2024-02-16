
palavraSecreta = str(input('Digite a palavra a ser descoberta:'))
print(palavraSecreta)

segredo = len(palavraSecreta) * '*'
print(segredo)
tentativas = 3

print(f"Voce ainda tem {tentativas} tentativas")


while tentativas >= 0 :
    letra = str(input('Chute uma letra:'))
    if letra in palavraSecreta:
        index = palavraSecreta.index(letra)
        new_string = list(segredo)
        new_string[index] = letra
        segredo = "".join(new_string)
        print(segredo)
    else:
        tentativas = tentativas - 1

    print(f"Voce ainda tem {tentativas} tentativas")

if tentativas < 0:
    print('Voce perdeu')
else:
    print('Voce ganhou')