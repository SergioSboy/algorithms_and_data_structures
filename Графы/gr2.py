import sys
sys.setrecursionlimit(30000000)
def dfs(v):
    global flag, path
    if flag == 1:
        return
    used[v] = 1
    path.append(v)

    for to in g[v]:
        if used[to] == 1:
            path.append(to)
            flag = 1
            return
        else:
            dfs(to)
            if flag == 1:
                return

    used[v] = 2
    path.pop()

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
used = [0] * (n+1)
flag = 0
path = []

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

for i in range(1, n+1):
    if used[i] == 0:
        dfs(i)
        if flag == 1:
            break

if flag == 1:
    i = len(path) - 2
    to = path[-1]
    while path[i] != to:
        i -= 1
    print(1)

else:
    print(0)