#Example of multiple heritage with python

class Animal:
    def __init__(self,nome)->None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"O {self.nome} está amamentando !!!"

class Ave(Animal):
    def voar(self):
        return f"O {self.nome} está voando !!!"

# Morcego class heritages from Mamifero and Ave
class Morcego(Mamifero,Ave):
    def emitir_som(self):
        return f"Morcegos emitem sons estranhos"

morcego = Morcego("Batman")

print(morcego.emitir_som())
print(morcego.voar())
print(morcego.amamentar())
