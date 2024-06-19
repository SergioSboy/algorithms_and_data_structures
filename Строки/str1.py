import sys

k = 31
mod = 10 ** 9 + 7
s = input()
N = int(input())
m = 1
n = len(s)
maxn = 10 ** 5 + 5

h = [0] * (len(s) + 1)
p = [0] * maxn
p[0] = 1
for i in range(1, maxn):
    p[i] = (p[i - 1] * k) % mod
for i in range(len(s)):
    h[i + 1] = (h[i] + p[i] * ord(s[i])) % mod


def hash_subs(l, r):
    return (h[r + 1] - h[l]) * p[n - l] % mod


for _ in range(N):
    a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
    if hash_subs(a1 - 1, b1 - 1) == hash_subs(a2 - 1, b2 - 1):
        print('Yes')
    else:
        print('No')
