# use of common decorators with python

class MinhaClasse:
    valor = 10
    def __init__(self,nome)->None:
        self.nome = nome

    def metodo_instancia(self):
        return f"Este metodo pertence a instancia da classe"
    
    @classmethod
    def metodo_classe(cls):
        return f"Este metodo pertence a classe que possui valor igual a {cls.valor}"

    @staticmethod
    def metodo_estatico():
        return f"Este metodo estatico da minha classe"

objeto = MinhaClasse("Luiz")
print(objeto.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

#example use of class Method
print("\nUso do decorator class Method")
class Carro:
    def __init__(self,modelo,marca,ano)->None:
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
    

    @classmethod
    def cria_carro(cls,configurations):
        modelo,marca,ano = configurations.split(",")
        return cls(modelo,marca,int(ano))

carro = Carro.cria_carro("Cobalt,Chevrolet,2013")

print(carro.modelo)
print(carro.marca)
print(carro.ano)

