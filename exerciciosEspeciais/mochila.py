def knapsack(values, weights, capacity):
    n = len(values)
    # Inicialize a tabela para armazenar os valores ótimos
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Construa a tabela de forma iterativa
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    # Reconstrua a solução
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return table[n][capacity], selected_items

# Exemplo de utilização:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack(values, weights, capacity)
print("Valor máximo da mochila:", max_value)
print("Itens selecionados:", selected_items)
