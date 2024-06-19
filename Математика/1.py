import math

def find_min_turns(N, K):
    # Вычисление наибольшего общего делителя (НОД)
    gcd = math.gcd(N, K)
    # Вычисление наименьшего общего кратного (НОК) с использованием формулы
    lcm = (N * K) // gcd
    return lcm

# Чтение входных данных
N, K = map(int, input().split())

# Нахождение минимального количества поворотов и вывод результата
result = find_min_turns(N, K)
print(result)