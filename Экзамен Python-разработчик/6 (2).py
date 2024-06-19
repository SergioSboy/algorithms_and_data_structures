from collections import deque


def knight_moves(n, m, start, end):
    # Инициализация доски
    board = [[float('inf')] * m for _ in range(n)]
    board[start[0]][start[1]] = 0

    # Возможные ходы коня
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Очередь для BFS
    queue = deque([start])

    # BFS
    while queue:
        x, y = queue.popleft()
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == float('inf'):
                board[nx][ny] = board[x][y] + 1
                queue.append((nx, ny))

    # Восстановление пути
    path = []
    x, y = end

    if board[x][y] == float('inf'):
        return float('inf'), []
    while board[x][y] != 0:
        path.append((x, y))
        for move in moves:
            nx, ny = x - move[0], y - move[1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[x][y] - 1:
                x, y = nx, ny
                break
    path.append(start)
    return board[end[0]][end[1]], path[::-1]


def king_moves(n, m, start, end):
    # Инициализация доски
    board = [[float('inf')] * m for _ in range(n)]
    board[start[0]][start[1]] = 0

    # Возможные ходы короля
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1),
             (1, 1), (-1, 1), (-1, -1), (1, -1)]

    # Рекурсивный проход
    for i in range(n):
        for j in range(m):
            for move in moves:
                x, y = i + move[0], j + move[1]
                if 0 <= x < n and 0 <= y < m:
                    board[x][y] = min(board[x][y], board[i][j] + 1)

    path = []
    x, y = end

    if board[x][y] == float('inf'):
        return float('inf'), []
    while board[x][y] != 0:
        path.append((x, y))
        for move in moves:
            nx, ny = x - move[0], y - move[1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[x][y] - 1:
                x, y = nx, ny
                break
    path.append(start)
    return board[end[0]][end[1]], path[::-1]

    path = []
    x, y = end
    if board[x][y] == float('inf'):
        return float('inf'), []
    while board[x][y] != 0:
        path.append((x, y))
        for move in moves:
            nx, ny = x - move[0], y - move[1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == board[x][y] - 1:
                x, y = nx, ny
                break
    path.append(start)
    return board[end[0]][end[1]], path[::-1]


def st(start, end, figure, m):
    if start == end:
        return m
    if figure == 'K':
        min_moves, path = knight_moves(n, n, start, end)
        if not path:
            return -1
        i = 0
        for i in range(len(path)):
            x, y = path[i]
            if 'G' == b[x][y]:
                m += i
                i = i
                figure = 'G'
                return st(path[i], end, figure, m)
        m += len(path) - 1
        return st(path[i], end, figure, m)
    if figure == 'G':

        min_moves, path = king_moves(n, n, start, end)
        if not path:
            return -1
        i = 0
        for i in range(len(path)):
            i = i
            x, y = path[i]
            if 'K' == b[x][y]:
                m += i
                figure = 'K'
                return st(path[i], end, figure, m)
        m += len(path) - 1
        return st(path[i], end, figure, m)


# Пример использования
n = int(input())
b = []
for i in range(n):
    s = input()
    b.append(list(s))
start_position = None
end_position = None
for i in range(n):
    for j in range(n):
        if b[i][j] == 'S':
            start_position = (i, j)
        if b[i][j] == 'F':
            end_position = (i, j)

if start_position and end_position:
    figure = 'K'  # Начинаем с коня
    moves = st(start_position, end_position, figure, 0)
    print(moves)


# Пример использования
"""
3
S.G
F..
.K.
"""

"""
4
S..K
..G.
.GK.
.K.F
"""

'''
2
SF
..
'''

"""
4
S..K
..G.
.KK.
.K.F
"""