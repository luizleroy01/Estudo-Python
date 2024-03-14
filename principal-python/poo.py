#use of object orientation with python

class Pessoa:
    def __init__(self,nome,idade)->None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos de idade"
    

pessoa1 = Pessoa("Luiz Eduardo",22)

mensagem = pessoa1.saudacao()

print(mensagem)