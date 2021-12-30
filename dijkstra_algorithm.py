# Реализация хеш таблиц
graph = {
    "A": {"B": 1},
    "B": {"E": 8, "D": 2, "C": 4},
    "C": {"B": 4, "E": 4},
    "D": {"B": 2, "E": 4},
    "E": {"B": 8, "C": 4},
}

costs = {
    "B": 1,
    "C": float("inf"),
    "D": float("inf"),
    "E": float("inf"),
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed: #Если узел с наим стоимостью уже из виденных и он еще не был обработан
            lowest_cost = cost # Он назначается новым узлом
            lowest_cost_node = node
    return lowest_cost_node

def find_lowest_way(graph, endPoint):
    node = find_lowest_cost_node(graph["A"]) # Найти узел с наименьшей стоимостью среди необработаных
    while node is not None: # Если обработаны все узлы цикл завершается
        cost = costs[node]
        neigbords = graph[node]
        for n in neigbords.keys(): # Перебрать всех соседей текущего узла
            new_cost = cost + neigbords[n]
            if costs[n] > new_cost:# Если соседу можно быстрее добратся через текущий узел
                costs[n] = new_cost # обновить стоимость этого узла
        processed.append(node)# Узел помечается как проеденный
        node = find_lowest_cost_node(graph[node])# Найти новый узел и повторить цикл
    return costs[endPoint]

print(find_lowest_way(graph, "E"))