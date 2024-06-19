def count_ships(N, M, grid):
    def dfs(x, y):
        stack = [(x, y)]
        ship_cells = []
        while stack:
            cx, cy = stack.pop()
            if not (0 <= cx < N and 0 <= cy < M) or used[cx][cy] or grid[cx][cy] == 0:
                continue
            used[cx][cy] = True
            ship_cells.append((cx, cy))
            for nx, ny in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
                stack.append((nx, ny))
        return ship_cells

    used = [[False] * M for _ in range(N)]
    ships = [0, 0, 0]  # counts for whole, damaged, and destroyed ships

    for i in range(N):
        for j in range(M):
            if grid[i][j] and not used[i][j]:
                used[i][j] = True
                vec = dfs(i, j)
                nS = sum(1 for x, y in vec if grid[x][y] == 1)
                nX = sum(1 for x, y in vec if grid[x][y] == 2)
                if nX == 0:
                    ships[0] += 1  # whole ship
                elif nS == 0:
                    ships[2] += 1  # destroyed ship
                else:
                    ships[1] += 1  # damaged ship

    return ships


# Чтение входных данных
N, M = map(int, input().split())
data = input().split()
grid = [[0] * M for _ in range(N)]
index = 2

for i in range(N):
    for j in range(M):
        x = data[index]
        index += 1
        if x == '-':
            grid[i][j] = 0
        elif x == 'S':
            grid[i][j] = 1
        elif x == 'X':
            grid[i][j] = 2

# Подсчет количества кораблей
whole_ships, damaged_ships, destroyed_ships = count_ships(N, M, grid)

# Вывод результатов
print(whole_ships, damaged_ships, destroyed_ships)
