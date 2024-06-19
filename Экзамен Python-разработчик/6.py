from collections import deque

def min_moves_to_reach_end(n, board):
    directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                  (2, 1), (2, -1), (-2, 1), (-2, -1)]
    start = None
    end = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == "S":
                start = (i, j)
            elif board[i][j] == "F":
                end = (i, j)

    queue = deque([(start, 0, False)])  # (position, moves, transformed)
    visited = set([start])

    while queue:
        pos, moves, transformed = queue.popleft()
        if pos == end:
            return moves

        x, y = pos
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if (nx, ny) not in visited:
                    if board[nx][ny] == ".":
                        visited.add((nx, ny))
                        queue.append(((nx, ny), moves + 1, transformed))
                    elif board[nx][ny] == "G" and not transformed:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), moves + 1, True))
                    elif board[nx][ny] == "K" and transformed:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), moves + 1, False))

    return -1

# Пример использования:
n = int(input())
board = []
for _ in range(n):
    s = input()
    l = []
    for i in s:
        l.append(i)
    board.append(l)
print(board)
result = min_moves_to_reach_end(n, board)
print(result)