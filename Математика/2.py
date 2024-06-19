import math
from collections import defaultdict

def prime_factors(N):
    factors = defaultdict(int)
    # Проверка делимости на 2
    while N % 2 == 0:
        factors[2] += 1
        N //= 2
    # Проверка делимости на все нечетные числа от 3 до sqrt(N)
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        while N % i == 0:
            factors[i] += 1
            N //= i
    # Если N является простым числом больше 2
    if N > 2:
        factors[N] += 1
    return factors

def format_factors(factors):
    result = []
    for prime in sorted(factors):
        if factors[prime] > 1:
            result.append(f"{prime}^{factors[prime]}")
        else:
            result.append(f"{prime}")
    return "*".join(result)

# Чтение входных данных
N = int(input().strip())

# Нахождение простых множителей
factors = prime_factors(N)

# Форматирование и вывод результата
output = format_factors(factors)
print(output)
