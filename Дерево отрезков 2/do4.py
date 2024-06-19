import sys

class Cord:
    def __init__(self, x, up, down, start):
        self.x = x
        self.up = up
        self.down = down
        self.start = start

class Node:
    def __init__(self):
        self.upd = False
        self.data = -sys.maxsize
        self.add = 0

def compare(x1, x2):
    return (x1.x < x2.x) or (x1.x == x2.x and (x1.start or not x2.start))

def push(v):
    if not t[v].upd:
        return

    if v * 2 + 1 < n + p - 1:
        if t[v * 2 + 1].upd:
            t[v * 2 + 1].add += t[v].add
        else:
            t[v * 2 + 1].upd = True
            t[v * 2 + 1].add = t[v].add

    if v * 2 + 2 < n + p - 1:
        if t[v * 2 + 2].upd:
            t[v * 2 + 2].add += t[v].add
        else:
            t[v * 2 + 2].upd = True
            t[v * 2 + 2].add = t[v].add

    t[v].upd = False
    t[v].data += t[v].add

def update(v, l, r, tl, tr, value):
    if l > tr or r < tl:
        return

    if tl >= l and r >= tr:
        push(v)

        if t[v].upd:
            t[v].add += value
        else:
            t[v].upd = True
            t[v].add = value

        push(v)
        tm = (tl + tr) // 2

        update(v * 2 + 1, l, r, tl, tm, value)
        update(v * 2 + 2, l, r, tm + 1, tr, value)

        left = t[v * 2 + 1].data + t[v * 2 + 1].add if t[v * 2 + 1].upd else t[v * 2 + 1].data
        right = t[v * 2 + 2].data + t[v * 2 + 2].add if t[v * 2 + 2].upd else t[v * 2 + 2].data

        t[v].data = max(left, right)

def build(v, tl, tr):
    if tl == tr:
        if v < n + p - 1:
            t[v].data = 0
            return

    tm = (tl + tr) // 2

    build(v * 2 + 1, tl, tm)
    build(v * 2 + 2, tm + 1, tr)

    t[v].data = max(t[v * 2 + 1].data, t[v * 2 + 2].data)

def cordY():
    max_val = t[0].data
    v = 0
    while v * 2 + 1 < n + p - 1:
        push(v)
        left = t[v * 2 + 1].data + t[v * 2 + 1].add if t[v * 2 + 1].upd else t[v * 2 + 1].data
        if left == max_val:
            v = v * 2 + 1
        else:
            v = v * 2 + 2
    return v

def upToDegree():
    global p
    while n > p:
        p = p << 1

def main():
    global n, p, t
    nn = int(input())
    p = 1

    x = []
    x.append(Cord(0, 0, 0, True))
    x.append(Cord(0, 0, 0, False))

    x[0].x, x[0].up, x[1].x, x[0].down = map(int, input().split())

    x[1].up = x[0].up
    x[1].down = x[0].down

    miny = x[0].up
    maxy = x[0].down

    for i in range(2, 2 * nn, 2):
        x_temp = Cord(0, 0, 0, True)
        x_temp.x, x_temp.up, x[i + 1].x, x_temp.down = map(int, input().split())

        x.append(x_temp)
        x.append(Cord(0, 0, 0, False))

        x[i + 1].up = x[i].up
        x[i + 1].down = x[i].down

        if miny > x[i].up:
            miny = x[i].up
        if maxy < x[i].down:
            maxy = x[i].down

    x.sort(key=lambda cord: (cord.x, cord.start), reverse=False)

    n = maxy + 1 - miny
    upToDegree()

    size = p << 1 - 1
    t = [Node() for _ in range(size)]

    build(0, 0, p - 1)

    answer = 0
    cordx = 0
    cordy = 0
    m = 0 - miny

    add = 1 if x[0].start else -1

    update(0, x[0].up + m, x[0].down + m, 0, p - 1, add)
    answer = t[0].data
    cordx = x[0].x
    cordy = x[0].up

    for i in range(1, len(x)):
        add = 1 if x[i].start else -1

        update(0, x[i].up + m, x[i].down + m, 0, p - 1, add)

        if answer < t[0].data:
            answer = t[0].data
            cordx = x[i].x
            cordy = cordY() - m - p + 1

    print(answer)
    print(cordx, cordy)

if __name__ == "__main__":
    main()
