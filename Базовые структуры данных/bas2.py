from collections import deque


def window(s, n, k):
    res = []
    w = deque()
    for i in range(n):
        while w and w[0] < i - k + 1:
            w.popleft()

        while w and s[i] < s[w[-1]]:
            w.pop()
        w.append(i)
        if i >= k - 1:
            res.append(s[w[0]])

    return res

n, k = map(int, input().split())
s = list(map(int, input().split()))

res = window(s, n, k)

print(*res)

'''
7 3
1 3 2 4 5 3 1
'''