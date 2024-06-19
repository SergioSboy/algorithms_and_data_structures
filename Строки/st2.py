import sys


def z_function(s, poisk):
    l = 0
    r = 0
    s = poisk + '#' + s
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            r = i + z[i] - 1
            l = i
    ans = []
    count = 0
    n_poisk = len(poisk)
    for i in range(n_poisk, n):
        if n_poisk == z[i]:
            count += 1
            ans.append(i - n_poisk - 1)
    return count, ans


T = sys.stdin.readline()
N = int(input())
for _ in range(N):
    s = sys.stdin.readline()
    count, ans = z_function(T, s)
    if count > 0:
        print(count, *ans)
    else:
        print(count)