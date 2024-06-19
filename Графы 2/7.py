from collections import defaultdict
import heapq

INF = float('inf')

def dijkstra(graph, start):
    distances = {node: INF for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1

    distances_from_a = dijkstra(graph, a)
    distances_from_b = dijkstra(graph, b)
    distances_from_c = dijkstra(graph, c)

    res = INF
    for i in range(n):
        distance_from_a_to_x = distances_from_a.get(i, INF)
        distance_from_b_to_x = distances_from_b.get(i, INF)
        distance_from_c_to_x = distances_from_c.get(i, INF)

        if distance_from_a_to_x != INF or distance_from_b_to_x != INF or distance_from_c_to_x != INF:
            min_distance = min(distance_from_a_to_x, distance_from_b_to_x, distance_from_c_to_x)
            if min_distance == distance_from_a_to_x:
                res = min(res, 2 * min_distance + distance_from_b_to_x + distance_from_c_to_x)
            if min_distance == distance_from_b_to_x:
                res = min(res, 2 * min_distance + distance_from_a_to_x + distance_from_c_to_x)
            if min_distance == distance_from_c_to_x:
                res = min(res, 2 * min_distance + distance_from_b_to_x + distance_from_a_to_x)

    if res != INF:
        print(res)
    else:
        print("-1")
