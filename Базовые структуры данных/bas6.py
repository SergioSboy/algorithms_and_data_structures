from collections import deque
import sys
queue = deque()
dct = {}
numerator = 0
for _ in range(int(sys.stdin.readline())):
    op, *v = sys.stdin.readline().split()
    op = int(op)
    if op in [1, 4]:
        p2 = int(v[0])
        if op == 1:
            queue.append((p2, numerator))
            dct[p2] = numerator
            numerator += 1
        else:
            print(dct[p2] - queue[0][1])
    else:
        if op == 2:
            pp = queue.popleft()
            del dct[pp[0]]
        elif op == 3:
            pp = queue.pop()
            del dct[pp[0]]
            numerator -= 1
        else: print(queue[0][0])



