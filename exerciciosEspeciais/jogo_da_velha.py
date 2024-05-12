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



game_table = create_game()

show_table(game_table)