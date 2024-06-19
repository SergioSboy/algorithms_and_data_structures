import sys
sys.setrecursionlimit(30000000)
def dfs(v):
    visited[v] = True
    components[-1].append(v)
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (N+1)
components = []

for v in range(1, N+1):
    if not visited[v]:
        components.append([])
        dfs(v)

print(len(components))
for component in components:
    component.sort()
    print(len(component))
    print(*component)