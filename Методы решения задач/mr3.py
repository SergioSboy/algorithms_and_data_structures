def can(A, N, D):
    occupiedCount = 1
    lastOccupiedPos = A[0]
    for i in A:
        if lastOccupiedPos + D > i:
            continue
        occupiedCount += 1
        lastOccupiedPos = i
    return occupiedCount >= N


l = 0
r = 100000000000000

N, K = map(int, input().split())
A = list(map(int, input().split()))
while r - l > 1:
    m = (l + r) // 2
    if can(A, K, m):
        l = m
    else:
        r = m
print(l)
