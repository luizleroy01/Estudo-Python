caractere = str(input())
texto = str(input())

palavras = texto.split(' ')
total_palavras = len(palavras)
cont_palavra = 0

for palavra in palavras:
    if caractere in palavra:
        cont_palavra+=1

porcentagem = (cont_palavra/total_palavras) * 100

print(format(porcentagem,".1f"))