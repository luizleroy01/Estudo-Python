#arquivo dedicado a manipulação de uma string 

nome = "Luiz Eduardo"

#iterando sobre a string com while
i = 0
nova_string = ""
while i <= len(nome):
    parte = f'{nome[i-1:i]}*'
    nova_string += parte
    i+=1

print(nova_string)