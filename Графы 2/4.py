n = int(input())
arr = [list(map(int, input().split())) for _ in range(1)]

prev = list(range(-1, n - 1))
next_ = list(range(1, n)) + [-1]

died = [-1] * n
life = set(range(n))

for k in range(n):
    die = set()
    for i in life:
        attack = 0
        if prev[i] != -1:
            attack += arr[prev[i]][0]
        if next_[i] != -1:
            attack += arr[next_[i]][0]
        if attack > arr[i][1]:
            die.add(i)
    life.clear()

    print(len(die), end=" ")

    for x in die:
        if prev[x] != -1:
            next_[prev[x]] = next_[x]
            if prev[x] not in die:
                life.add(prev[x])
        if next_[x] != -1:
            prev[next_[x]] = prev[x]
            if next_[x] not in die:
                life.add(next_[x])
