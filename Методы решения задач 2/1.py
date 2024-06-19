import sys
from collections import defaultdict

MAX = 200001
LOGMAX = 20

n, l = 0, 0
g = defaultdict(list)
tin = [0] * MAX
tout = [0] * MAX
timer = 0
up = [[0] * LOGMAX for _ in range(MAX)]


def dfs(v, p=1):
    global timer
    tin[v] = timer
    timer += 1
    up[v][0] = p

    for i in range(1, l + 1):
        up[v][i] = up[up[v][i - 1]][i - 1]

    for to in g[v]:
        if to != p:
            dfs(to, v)

    tout[v] = timer
    timer += 1


def upper(a, b):
    return tin[a] <= tin[b] and tout[a] >= tout[b]


def lca(a, b):
    if upper(a, b):
        return a

    if upper(b, a):
        return b

    for i in range(l, -1, -1):
        if not upper(up[a][i], b):
            a = up[a][i]

    return up[a][0]


def main():
    global n, l
    n = int(sys.stdin.readline())

    l = 1
    while (1 << l) <= n:
        l += 1

    x = list(map(int, sys.stdin.readline().split()))
    for i in range(2, n + 1):
        g[x[i-2] + 1].append(i)

    dfs(1)

    m = int(sys.stdin.readline())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        res = lca(u + 1, v + 1)
        print(res - 1)


if __name__ == "__main__":
    main()
