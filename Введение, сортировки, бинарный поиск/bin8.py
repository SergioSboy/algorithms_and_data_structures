def f(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


def secant_method(a, b, c, d):
    x0 = -100000
    x1 = 100000
    epsilon = 1e-12

    while abs(x1 - x0) >= epsilon:
        x2 = x1 - f(x1, a, b, c, d) * (x1 - x0) / (f(x1, a, b, c, d) - f(x0, a, b, c, d))
        x0 = x1
        x1 = x2
    return f'{x2:.4f}'


a, b, c, d = map(int, input().split())
root = secant_method(a, b, c, d)
print(root)
