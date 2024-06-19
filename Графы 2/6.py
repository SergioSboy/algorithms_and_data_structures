import heapq


def dijkstra(graph, start, end, truck_capacity):
    # Инициализация расстояний до вершин и количества кружек, которые можно взять на каждой дороге
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    max_cups = {node: float('inf') for node in graph}
    max_cups[start] = truck_capacity

    # Приоритетная очередь для хранения вершин и их расстояний
    pq = [(0, start)]

    while pq:
        dist, current = heapq.heappop(pq)

        if current == end:
            return max_cups[end]  # Возвращаем количество кружек, которые можно взять на ЛКШ

        if dist > distance[current]:
            continue

        for neighbor, weight, max_weight in graph[current]:
            weight += 3  # Добавляем вес пустого грузовика
            if weight <= max_weight and max_cups[current] < max_cups[neighbor]:
                max_cups[neighbor] = min(max_cups[current], (max_weight - weight) // 100)
                distance[neighbor] = dist + weight
                heapq.heappush(pq, (dist + weight, neighbor))

    return max_cups[end]  # Если путь не найден


# Функция для чтения входных данных с клавиатуры
def read_input():
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v, time, max_weight = map(int, input().split())
        graph[u].append((v, time, max_weight))
        graph[v].append((u, time, max_weight))
    return graph


if __name__ == "__main__":
    print("Введите количество узловых пунктов и количество дорог:")
    graph = read_input()
    truck_capacity = 1000000000 - 3000  # Вместимость грузовика с учетом пустого веса
    max_cups = dijkstra(graph, 1, len(graph), truck_capacity)
    print("Максимальное количество кружек, которое можно привезти за первый рейс:", max_cups)
