import collections


q1 = collections.deque()
q2 = collections.deque()
for _ in range(int(input())):

    c = input().split()

    if c[0] == '+':
        q2.append(c[1])
    elif c[0] == '*':
        q2.appendleft(c[1])
    else:
        print(q1.popleft())

    if len(q1) < len(q2):
        q1.append(q2.popleft())