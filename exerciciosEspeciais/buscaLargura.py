import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state  # Estado do nó
        self.parent = parent  # Nó pai
        self.g = g  # Custo do caminho do nó inicial até este nó
        self.h = h  # Heurística (custo estimado do nó até o objetivo)

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar_search(initial_state, goal_test, successors, heuristic):
    open_list = []  # Lista de nós a serem explorados
    closed_set = set()  # Conjunto de nós já explorados

    # Adiciona o nó inicial à lista de nós a serem explorados
    heapq.heappush(open_list, Node(initial_state, None, 0, heuristic(initial_state)))

    # Loop principal
    while open_list:
        current_node = heapq.heappop(open_list)  # Remove e retorna o nó com menor valor de f(n)

        if goal_test(current_node.state):
            path = []  # Lista para armazenar o caminho da solução
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]  # Retorna o caminho da solução

        closed_set.add(current_node.state)  # Marca o nó como explorado

        for child_state, cost in successors(current_node.state):
            if child_state in closed_set:  # Se o nó já foi explorado, ignora
                continue
            g = current_node.g + cost  # Custo atualizado do caminho até o nó filho
            h = heuristic(child_state)  # Heurística para o nó filho
            child_node = Node(child_state, current_node, g, h)
            heapq.heappush(open_list, child_node)  # Adiciona o nó filho à lista de nós a serem explorados

    return None  # Retorna None se não houver solução encontrada

# Exemplo de utilização:

# Função de teste de objetivo
def goal_test(state):
    return state == 'G'

# Função para calcular os sucessores de um estado
def successors(state):
    if state == 'S':
        return [('A', 1), ('B', 3)]
    elif state == 'A':
        return [('G', 1)]
    elif state == 'B':
        return [('G', 3)]
    else:
        return []

# Função heurística (admissível)
def heuristic(state):
    h_values = {'S': 0, 'A': 2, 'B': 3, 'G': 0}  # Valores das heurísticas para cada estado
    return h_values[state]

# Chamada da função de busca A*
path = astar_search('S', goal_test, successors, heuristic)
print("Caminho da solução encontrado:", path)
