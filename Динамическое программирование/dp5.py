def damerau_levenshtein_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        matrix[i][0] = i

    for j in range(len2 + 1):
        matrix[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j] + 1,  # удаление
                               matrix[i][j - 1] + 1,  # вставка
                               matrix[i - 1][j - 1] + cost)  # замена
            if i > 1 and j > 1 and str1[i - 1] == str2[j - 2] and str1[i - 2] == str2[j - 1]:
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + cost)  # перестановка

    return matrix[len1][len2]


# Пример использования:
str1 = input()
str2 = input()
print(damerau_levenshtein_distance(str1, str2))
