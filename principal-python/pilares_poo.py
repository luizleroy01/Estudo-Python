#basics of object programming using python

#example of heritage

class Animal:
    def __init__(self,nome)->None:
        self.nome = nome
    
    def andar(self):
        print(f"O {self.nome} andou !!!")
    
    def emitir_som(self):
        pass

# Cachorro class heritages methods and fields from Animal
class Cachorro(Animal):
    def emitir_som(self):
        return "Au,Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!!"

cachorro = Cachorro('cachorro')
gato = Gato('gato')

cachorro.andar()
gato.andar()

som_cachorro = cachorro.emitir_som()
som_gato = gato.emitir_som()

print(som_cachorro,som_gato) 

animais = [cachorro,gato]

for animal in animais:
    print(f"O {animal.nome} faz {animal.emitir_som()}")

#Example of encapsulation 

print("\nExemplo de encapsulamento com python")

class ContaBancaria:
    def __init__(self,saldo)->None:
        # private attribute of ContaBancaria
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"O valor {valor} foi adicionado a sua conta")
    
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"O valor {valor} foi debitado de sua conta")
        else:
            print("Saldo insuficiente no momento")
    
    def mostrar_saldo(self):
        print(f"Seu saldo atual é de : R$ {conta.get_saldo()}")
    

conta = ContaBancaria(100)
conta.mostrar_saldo()
conta.depositar(35)
conta.mostrar_saldo()
conta.depositar(58)
conta.mostrar_saldo()
conta.sacar(230)
conta.sacar(97)
conta.mostrar_saldo()

#Example of abstraction with python and object orientation
print("\nExemplo de abstração com Python")

from abc import ABC,abstractmethod

class Veiculo(ABC):
    #use of decorators
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self,nome)->None:
        self.nome = nome
    
    def ligar(self):
        print(f"Ligar carro {self.nome} com a chave")
    
    def desligar(self):
        print(f"Desligar carro {self.nome} com a chave")

carro = Carro("Argo Trekking")
carro.ligar()
carro.desligar()
