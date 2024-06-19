from collections import deque

class Posl:
    def __init__(self, p, size):
        self.p = p
        self.size = size

def to_the_infinity_and_beyond(a):
    n = len(a)
    prev = [-1] * n
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + 1:
                prev[i] = j
                dp[i] = dp[j] + 1

    last = 0
    length = dp[0]

    for i in range(n):
        if length < dp[i]:
            last = i
            length = dp[i]

    ans = deque()
    while last >= 0:
        cur = a[last]
        ans.appendleft(cur)
        last = prev[last]

    return Posl(ans, length)


n = int(input())
a = list(map(int, input().split()))

result = to_the_infinity_and_beyond(a)
print(result.size)
print(*result.p)
