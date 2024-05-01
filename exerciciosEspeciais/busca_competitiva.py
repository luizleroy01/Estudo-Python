def minimax(tabuleiro, jogador):
    if vencedor(tabuleiro, 'X'):
        return None, 1 if jogador == 'X' else -1
    if vencedor(tabuleiro, 'O'):
        return None, -1 if jogador == 'X' else 1
    if not movimentos_possiveis(tabuleiro):
        return None, 0

    melhor_pontuacao = float('-inf') if jogador == 'X' else float('inf')
    melhor_movimento = None
    for movimento in movimentos_possiveis(tabuleiro):
        i, j = movimento
        tabuleiro[i][j] = jogador
        _, pontuacao = minimax(tabuleiro, 'O' if jogador == 'X' else 'X')
        tabuleiro[i][j] = None
        if (jogador == 'X' and pontuacao > melhor_pontuacao) or (jogador == 'O' and pontuacao < melhor_pontuacao):
            melhor_pontuacao = pontuacao
            melhor_movimento = movimento

    return melhor_movimento, melhor_pontuacao

def jogar_minimax(tabuleiro):
    while not jogo_terminado(tabuleiro):
        movimento, _ = minimax(tabuleiro, 'X')
        if movimento:
            i, j = movimento
            tabuleiro[i][j] = 'X'
            if jogo_terminado(tabuleiro):
                break
            imprimir_tabuleiro(tabuleiro)
        movimento, _ = minimax(tabuleiro, 'O')
        if movimento:
            i, j = movimento
            tabuleiro[i][j] = 'O'
        imprimir_tabuleiro(tabuleiro)
    imprimir_tabuleiro(tabuleiro)
    print("Jogo terminado!")
