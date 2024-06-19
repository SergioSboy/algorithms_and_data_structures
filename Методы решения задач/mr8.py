def solve_olympiad(n, c, tasks):
    # Сортируем задачи по времени появления
    tasks.sort(key=lambda x: x[1])  # Сортируем по времени окончания

    total_points = 0  # Общее количество баллов
    selected_tasks = []  # Список выбранных задач

    time = 1  # Текущее время

    for i in range(n):
        start, end, index = tasks[i]
        # Проверяем, доступна ли задача в текущий момент времени
        if start >= time:
            # Добавляем задачу в список выбранных, увеличиваем количество баллов
            selected_tasks.append(index)
            total_points += c
            # Обновляем текущее время
            time = end

    return total_points, len(selected_tasks), selected_tasks


# Чтение входных данных
n, c = map(int, input().split())
tasks = []
for i in range(n):
    start, duration = map(int, input().split())
    end = start + duration
    tasks.append((start, end, i + 1))

# Решение задачи
max_points, num_selected, selected_tasks = solve_olympiad(n, c, tasks)

# Вывод результатов
print(max_points)
print(num_selected)
print(*selected_tasks)