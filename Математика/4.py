def last_nonzero_digit_factorial(n):
    last_nonzero_digit = 1
    count2, count5 = 0, 0

    for i in range(1, n + 1):
        current = i
        while current % 2 == 0:
            count2 += 1
            current //= 2
        while current % 5 == 0:
            count5 += 1
            current //= 5
        last_nonzero_digit = (last_nonzero_digit * current) % 10

    # Уравновесим количество 2 и 5, так как каждая пара 2 и 5 дает 10
    for _ in range(count2 - count5):
        last_nonzero_digit = (last_nonzero_digit * 2) % 10

    return last_nonzero_digit


# Чтение входных данных
n = int(input().strip())

# Вывод результата
print(last_nonzero_digit_factorial(n))
