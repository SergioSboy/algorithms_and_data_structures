import heapq

def prim(graph):
    # Стартовая вершина (можно выбрать любую)
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])
    edges = graph[start_vertex]  # Ребра, выходящие из стартовой вершины
    heapq.heapify(edges)  # Преобразуем список ребер в кучу для быстрого доступа к минимальному элементу
    minimum_spanning_tree_weight = 0  # Вес остовного дерева
    while edges:
        weight, vertex1, vertex2 = heapq.heappop(edges)  # Берем ребро с минимальным весом
        if vertex2 not in visited:
            visited.add(vertex2)
            minimum_spanning_tree_weight += weight
            for edge in graph[vertex2]:  # Добавляем новые ребра, выходящие из новой вершины
                if edge[2] not in visited:
                    heapq.heappush(edges, edge)
    return minimum_spanning_tree_weight

# Чтение входных данных
n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    bi, ei, wi = map(int, input().split())
    graph[bi].append((wi, bi, ei))
    graph[ei].append((wi, ei, bi))

# Выполнение алгоритма Прима и вывод результата
result = prim(graph)
print(result)