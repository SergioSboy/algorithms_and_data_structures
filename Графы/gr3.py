def is_topological_sort(graph, permutation):
    index_map = {node: index for index, node in enumerate(permutation)}

    for node in graph:
        for neighbor in graph[node]:
            if index_map[node] > index_map[neighbor]:
                return "NO"

    return "YES"


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

permutation = list(map(int, input().split()))

result = is_topological_sort(graph, permutation)
print(result)