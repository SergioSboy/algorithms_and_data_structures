def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inverse(a, mod):
    return mod_exp(a, mod - 2, mod)

def password_cracking_time(N, M, K, MOD):
    # M^N % MOD
    M_power_N = mod_exp(M, N, MOD)
    # K^-1 % MOD
    K_inv = mod_inverse(K, MOD)
    # (M^N * K^-1) % MOD
    result = (M_power_N * K_inv) % MOD
    return result

# Чтение входных данных
N, M, K, MOD = map(int, input().strip().split())

# Вычисление и вывод результата
print(password_cracking_time(N, M, K, MOD))
