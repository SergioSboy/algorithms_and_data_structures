from collections import deque

n_moves = int(input())

move = {}  # для реакций

for _ in range(n_moves):
    move_input = input().split(" -> ")
    from_move, to_move = move_input[0], move_input[1]
    if from_move not in move:
        move[from_move] = []
    move[from_move].append(to_move)

from_move = input()
to_move = input()

len_map = {}
q = deque()

len_map[from_move] = 0  # стартовую позицию в map
q.append(from_move)  # и в очередь

while q:
    cur = q.popleft()  # достаем из очереди очередную хрень

    if cur == to_move:
        print(len_map[cur])  # мы нашли всю цепочку и печатаем ее длину
        break

    for next_move in move.get(cur, []):  # по массиву с реакциями для этой хрени
        if next_move not in len_map:  # если в len_map такой записи вообще нет
            len_map[next_move] = len_map[cur] + 1  # то нужно ее создать
            q.append(next_move)
else:
    print(-1)