MOD = 10 ** 9 + 7


def mod_inverse(a, p):
    # Функция для вычисления a^(p-2) % p
    return pow(a, p - 2, p)


def prepare_factorials_and_inverses(n, mod):
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)

    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact[n] = mod_inverse(fact[n], mod)

    for i in range(n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    return fact, inv_fact


def binomial_coefficient(n, k, mod):
    if k > n:
        return 0
    fact, inv_fact = prepare_factorials_and_inverses(n, mod)
    return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod


# Чтение входных данных
n, k = map(int, input().strip().split())

# Вычисление и вывод биномиального коэффициента
print(binomial_coefficient(n, k, MOD))
