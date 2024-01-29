#codigo para identificar anagramas em python

from itertools import permutations

def encontrar_anagramas(palavra):
    # Gera todas as permutações da palavra
    permutacoes = [''.join(p) for p in permutations(palavra)]
    
    # Filtra as permutações para remover a palavra original
    anagramas = [p for p in permutacoes if p != palavra]
    
    return anagramas

# Exemplo de uso
palavra_exemplo = "barata"
resultado = encontrar_anagramas(palavra_exemplo)

print(f"Anagramas de {palavra_exemplo}: {resultado}")
