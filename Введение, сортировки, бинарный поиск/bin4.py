import math

C = float(input())


def f(x):
    return x ** 2 + math.sqrt(x + 1)


low = 0.0
high = C
eps = 1e-6

while high - low > eps:
    mid = (low + high) / 2
    if f(mid) < C:
        low = mid
    else:
        high = mid

print(f"{mid:.6f}")