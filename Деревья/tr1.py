

from collections import deque


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([(start, 0)])
    max_dist_node = start
    max_dist = 0

    while queue:
        node, dist = queue.popleft()
        visited[node] = True

        if dist > max_dist:
            max_dist = dist
            max_dist_node = node

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append((neighbor, dist + 1))

    return max_dist_node, max_dist


n = int(input())
parents = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for i in range(1, n):
    graph[i].append(parents[i - 1])
    graph[parents[i - 1]].append(i)

farthest_node, _ = bfs(graph, 0)
_, diameter = bfs(graph, farthest_node)

ans = [0]
for i, elem in enumerate(parents):
    ans.append(ans[elem] + 1)

print(max(ans), diameter)
print(*ans)

'''
7
0 0 1 1 1 2
'''

'''
6
0 1 2 2 2
'''
