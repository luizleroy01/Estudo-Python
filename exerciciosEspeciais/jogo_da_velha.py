def create_game():
    tabuleiro = list()

    for i in range(0, 3):
        line = list()
        for j in range(0, 3):
            line.append("*")

        tabuleiro.append(line)

    return tabuleiro


def show_table(tabuleiro):
    for i in range(0, 3):
        for j in range(0, 3):
            print(tabuleiro[i][j], end=" ")

        print()


def game_loop(tabuleiro, player1):
    if player1:
        jogadap1 = jogada_rodada(player1)

    linha = jogadap1[0]
    coluna = jogadap1[1]

    tabuleiro[linha][coluna] = "X"
    return tabuleiro


def jogada_rodada(verifyPlayer):
    linha = int(input("Digite a linha:"))
    coluna = int(input("Digite a coluna:"))
    posicao_tabuleiro = linha, coluna

    return posicao_tabuleiro


def verify_table(tabuleiro):
    disponible_positions = []

    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if tabuleiro[i][j] == "*":
                position = i, j
                disponible_positions.append(position)
        
        return disponible_positions


isPlayer1 = False
game_table = create_game()

show_table(game_table)

game_table = game_loop(game_table, True)

show_table(game_table)
