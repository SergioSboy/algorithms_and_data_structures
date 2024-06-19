class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def get(self):
        return self.stack[-1]

    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def getMa(self):
        return self.stack


def count_destroyed_balls(balls):
    if len(balls) < 3:
        return 0
    b = MinStack()
    destroyed = 0
    i = 0
    n = len(balls)
    while i < n:
        if b.empty():
            b.push((balls[i], 1))
        elif b.get()[0] != balls[i]:
            if b.get()[1] >= 3:
                t = b.get()[1]
                for k in range(t):
                    b.pop()
                    destroyed += 1
                if b.get()[0] == balls[i]:
                    b.push((balls[i], b.get()[1] + 1))

                else:
                    b.push((balls[i], 1))

            else:
                b.push((balls[i], 1))
        elif b.get()[0] == balls[i]:
            b.push((balls[i], b.get()[1] + 1))

        i += 1
    if b.get()[1] >= 3:
        t = b.get()[1]
        for k in range(t):
            b.pop()
            destroyed += 1
    return destroyed


if __name__ == "__main__":
    balls_count = int(input())
    balls_colors = list(map(int, input().split()))

    destroyed_count = count_destroyed_balls(balls_colors)
    print(destroyed_count)

'''
10
3 3 2 1 1 1 2 2 3 3
'''
