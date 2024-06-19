def largest_square(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Создаем матрицу для хранения промежуточных результатов
    dp = [[0] * m for _ in range(n)]

    # Заполняем первую строку и первый столбец матрицы dp
    for i in range(n):
        dp[i][0] = matrix[i][0]
    for j in range(m):
        dp[0][j] = matrix[0][j]

    # Вычисляем остальные значения матрицы dp
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    # Находим максимальное значение в матрице dp
    max_size = 0
    max_i = 0
    max_j = 0
    for i in range(n):
        for j in range(m):
            if dp[i][j] > max_size:
                max_size = dp[i][j]
                max_i = i - max_size + 1
                max_j = j - max_size + 1

    return max_size, max_i, max_j

# Чтение входных данных
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Вызов функции и вывод результата
size, row, col = largest_square(matrix)
print(size)
print(row + 1, col + 1)
