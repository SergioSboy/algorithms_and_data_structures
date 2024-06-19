def rotate_r(matrix):
    row = len(matrix)
    k = (row // 2 * row) + ((row * row) - row) // 2
    print(k)
    # Вывод количества и самих пар
    for i in range(row):
        for j in range(i + 1):
            if i != j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(i, j, j, i)

    # Переворачивание строк
    for i in range(len(matrix)):
        start = 0
        end = n - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            print(i, start, i, end)
            start += 1
            end -= 1
    return


def rotate_l(matrix):
    row = len(matrix)
    k = (row // 2 * row) + ((row * row) - row) // 2
    print(k)
    # Переворачивание строк
    for i in range(n):
        start = 0
        end = n - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            print(i, start, i, end)
            start += 1
            end -= 1
    # Выворачивание главной диагонали
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(i, j, j, i)
    # Вывод количества и самих пар

    return


n, rotate = input().split()
n = int(n)
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
if rotate == 'R':
    rotate_r(matrix)
else:
    rotate_l(matrix)
