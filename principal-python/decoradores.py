#Decorators are methods that change how a function is executed

def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    
    return wrapper

@meu_decorador
def minha_func():
    print("Função executada chamada por Luiz Eduardo Leroy")

minha_func()

# using a class to create a Decorator
class MinhaClasseDecorator:
    def __init__(self,func)->None:
        self.func = func

    def __call__(self)-> None:
        print("Antes da segunda função ser chamada(decorador de classe)")
        self.func()
        print("Depois da segunda função ser chamada(decorador de classe)")
    
@MinhaClasseDecorator
def segunda_funcao()->None:
    print("Chamada da segunda função")

segunda_funcao()


