import sys

N, M, K = map(int, sys.stdin.readline().split())
A = []
pref = [[0] * M for _ in range(N)]
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
pref[0][0] = A[0][0]
for i in range(1, M):
    pref[0][i] = pref[0][i - 1] + A[0][i]
for i in range(1, N):
    pref[i][0] = pref[i - 1][0] + A[i][0]
for i in range(1, N):
    for j in range(1, M):
        pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + A[i][j]


def query(y1, x1, y2, x2):
    return pref[x2][y2] \
        - (pref[x1 - 1][y2] if x1 > 0 else 0) \
        - (pref[x2][y1 - 1] if y1 > 0 else 0) \
        + (pref[x1 - 1][y1 - 1] if x1 > 0 and y1 > 0 else 0)


for i in range(K):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().split())
    print(query(x1-1, y1-1, x2-1, y2-1))
