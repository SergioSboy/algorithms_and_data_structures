from collections import deque


def min_moves_knight_path(N, x1, y1, x2, y2):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    queue = deque([(x1, y1, [])])  # Начальная позиция и путь
    visited = set((x1, y1))

    while queue:
        x, y, path = queue.popleft()

        if x == x2 and y == y2:
            return [len(path)] + [(x1, y1)] + path

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 < new_x <= N and 0 < new_y <= N and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, path + [(new_x, new_y)]))

    return None


# Пример использования
N = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
result = min_moves_knight_path(N, x1, y1, x2, y2)
if result:
    print(result[0])
    for x, y in result[1:]:
        print(x, y)
else:
    print(-1)