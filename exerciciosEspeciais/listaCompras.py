#xercicio lista de compras em python

#inicia a lista vazia
lista = []

resposta = str(input("Selecione:[i]inserir [a]apagar [l]istar [f]inalizar\n"))
while resposta != 'f':
    if resposta == 'i':
        item = str(input("Digite o  item:\n"))
        lista.append(item)
        print("Item inserido na lista")
    elif resposta == 'a':
        index = 0
        try:
            index = int(input("Digite qual indice da lista\n"))
        except:
            print("O valor digitado não é inteiro")
            index = int(input("Digite novamente o indice:\n"))
        
        if index <= len(lista):
            del lista[index]
        else:
            print("Indice inexistente na lista")
    elif resposta == 'l':
        if(len(lista) > 0):
            for index,nome in enumerate(lista):
                print(index,nome)
        else:
            print("A lista está vazia")
    elif resposta == 'f':
        break

    resposta = str(input("Selecione:[i]inserir [a]apagar [l]istar [f]inalizar\n"))

print("A lista és encerrada")