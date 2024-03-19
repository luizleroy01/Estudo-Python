#Turn game that consists ona battle between a hero and a vilain
import random
class Personagem:
    def __init__(self,nome,vida,nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} Vida: {self.get_vida()} Nivel: {self.get_nivel()}"

    def atacar(self,alvo):
        dano = random.randint(self.get_nivel() * 2,self.get_nivel() * 4)
        print(f"O {self.get_nome()} atacou o {alvo.get_nome()} e causou {dano} de dano")
        alvo.set_vida(dano)

    def set_vida(self,dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0


class Heroi(Personagem):
    def __init__(self,nome,vida,nivel,habilidade)->None:
        super().__init__(nome,vida,nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} Habilidade: {self.get_habilidade()}"
    
    def ataque_especial(self,alvo):
        dano = random.randint(self.get_nivel() * 5,self.get_nivel() * 8) #dano aumentado
        alvo.set_vida(dano)
        print(f"O {self.get_nome()} usou a habilidade especial {self.get_habilidade()} no {alvo.get_nome()} e causou {dano} de dano ")
    


class Inimigo(Personagem):
    def __init__(self,nome,vida,nivel,tipo)->None:
        super().__init__(nome,vida,nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} Tipo: {self.get_tipo()}"



class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self)->None:
        self.heroi = Heroi(nome="Super Man",vida=100,nivel=5,habilidade="Super Força")
        self.inimigo = Inimigo(nome="Darkside",vida=50,nivel=3,tipo="Corpo a corpo")

    def iniciar_batalha(self):
        """ fazer gestão da batlha em turnos """
        print("Iniciar batalha")

        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar ...")
            escolha = int(input("Escolha (1 - Ataque normal) (2-Ataque especial):"))
            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Opcao de ataque inválida ... tente novamente")
                escolha = int(input("Escolha (1 - Ataque normal) (2-Ataque especial):"))
                if escolha == 1:
                    self.heroi.atacar(self.inimigo)
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
        
        if(self.heroi.get_vida() > 0):
            print("parabens !!! voce venceu a batalha")
        else:
            print("Voce foi derrotado !!!")


jogo = Jogo()
jogo.iniciar_batalha()

            



