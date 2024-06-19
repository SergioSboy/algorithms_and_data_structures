def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_num + 1) if is_prime[p]]
    return is_prime, primes


def goldbach_partition(n):
    is_prime, primes = sieve_of_eratosthenes(n)

    for p in primes:
        q = n - p
        if q >= p and is_prime[q]:
            return p, q


# Чтение входного числа
n = int(input().strip())

# Найти и вывести два простых числа p и q, таких что p + q = n
p, q = goldbach_partition(n)
print(p, q)
