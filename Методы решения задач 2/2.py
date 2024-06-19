import sys

MAX = 200001
LOGMAX = 20

n, l = 0, 0
g = [[] for _ in range(MAX)]
tin = [0] * MAX
tout = [0] * MAX
timer = 0
up = [[(0, sys.maxsize)] * LOGMAX for _ in range(MAX)]


def dfs(v, p=1, c=sys.maxsize):
    global timer
    tin[v] = timer
    timer += 1
    up[v][0] = (p, c)
    for i in range(1, l + 1):
        up[v][i] = (up[up[v][i - 1][0]][i - 1][0],
                    min(up[v][i - 1][1], up[up[v][i - 1][0]][i - 1][1]))
    for to, cost in g[v]:
        dfs(to, v, cost)
    tout[v] = timer
    timer += 1


def upper(a, b):
    return tin[a] <= tin[b] and tout[a] >= tout[b]


def minlca(a, b):
    res = sys.maxsize
    for i in range(l, -1, -1):
        if not upper(up[a][i][0], b):
            res = min(res, up[a][i][1])
            a = up[a][i][0]
    if not upper(a, b):
        res = min(res, up[a][0][1])
    for i in range(l, -1, -1):
        if not upper(up[b][i][0], a):
            res = min(res, up[b][i][1])
            b = up[b][i][0]
    if not upper(b, a):
        res = min(res, up[b][0][1])
    return res


def main():
    global n, l
    n = int(sys.stdin.readline().strip())

    l = 1
    while (1 << l) <= n:
        l += 1

    for i in range(2, n + 1):
        x, p = map(int, sys.stdin.readline().split())
        g[x + 1].append((i, p))

    dfs(1)

    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        res = minlca(u + 1, v + 1)
        print(res)


if __name__ == "__main__":
    main()
