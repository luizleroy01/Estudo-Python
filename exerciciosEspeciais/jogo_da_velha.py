def create_game():
    tabuleiro = list()

    for i in range(0,3):
        line = list()
        for j in range(0,3):
            line.append("*")
        
        tabuleiro.append(line)

    
    return tabuleiro

def show_table(tabuleiro):
    for i in range(0,3):
        for j in range(0,3):
            print(tabuleiro[i][j],end=" ")
        
        print()


def game_loop(tabuleiro):
    p1 = str("Digite a posicao da sua jogada")
    respP1 = p1.split(" ")

    linha = int(respP1[0])
    coluna = (respP1[1])

    tabuleiro[linha][coluna] = "X"
    return tabuleiro


game_table = create_game()

show_table(game_table)

game_table = game_loop(game_table)

show_table(game_table)