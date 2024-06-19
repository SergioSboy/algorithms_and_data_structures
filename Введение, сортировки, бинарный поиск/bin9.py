
def podriad(n, a):
    m = 0
    while n >= 0:
        if a[n] == 1:
            m += 1
        else:
            return m, n
        n -= 1
    return m, n


def solve(n, p):
    a = [0] * n
    ans = [1]
    m = 0
    k = n - 1
    for i in range(n):
        index_to_change = p[i] - 1
        a[index_to_change] = 1
        if index_to_change == k:
            last_m = m
            m, k = podriad(k, a)
            m = last_m + m
        ans.append(1 + i + 1 - m)
    return ans


n = int(input())
p = list(map(int, input().split()))
result = solve(n, p)
print(*result)
