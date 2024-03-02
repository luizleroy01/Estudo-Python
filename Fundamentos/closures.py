#an example of closures with python

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Eduardo'))

for nome in ['Luiz','Heider','Marcia','Maria']:
    print(falar_bom_dia(nome))
    if nome == 'Maria':
        print(falar_boa_noite(nome))


# exercise using closure to calculate double,triple and multiply 4 times a same number

def cria_multiplicador(multiplicador):
    def multiplicar(num):
        return num * multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
triplicar = cria_multiplicador(3)
quadruplicar = cria_multiplicador(4)

print(duplicar(208))
print(triplicar(53))
print(quadruplicar(225))