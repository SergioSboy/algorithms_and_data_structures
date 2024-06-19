import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
pr = [0]
prXOR = [0]
for i in range(n):
    pr.append(pr[i] + A[i])
for i in range(n):
    prXOR.append(prXOR[i] ^ A[i])
for i in range(int(sys.stdin.readline())):
    q, l, r = map(int, sys.stdin.readline().split())
    if q == 2:
        if l > 0:
            print(prXOR[r] ^ prXOR[l - 1])
        else:
            print(prXOR[r])
    else:
        if l > 0:
            print(pr[r] - pr[l - 1])
        else:
            print(pr[r])

