#funções que recebem uma função por parâmetro e executam uma
#função
def bomDia(msg,*args):
    if args:
        print(args)
    elif msg is not None:
        print(msg)
    else:
        print('Bom dia!')
    

def executa(metodo,msg=None,*args):
    return metodo(msg,*args)

#as funções também se tornam um objeto que pode ser passado por
#parâmetro
executa(bomDia,"aprendendo python")
executa(bomDia)
executa(bomDia,None,"frase1")