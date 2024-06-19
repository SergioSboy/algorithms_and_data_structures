import sys
sys.stdin.readline()
inputs = map(int, sys.stdin.readline().split())
stack = []
mul_of_min_and_sum = 0
for num in inputs:
    if len(stack) > 0:
        last = stack[-1]
        if num < last[0]:
            acc = 0
            while len(stack) > 0 and stack[-1][0] > num:
                pp = stack.pop()
                acc += pp[1]
                mul_of_min_and_sum = max(mul_of_min_and_sum, pp[0] * acc)
            stack.append((num, acc + num))
        elif num > last[0]:
            stack.append((num, num))
        else:
            stack[-1] = (num, last[1] + num)
    else:
        stack.append((num, num))
acc = 0
while len(stack) > 0:
    pp = stack.pop()
    acc += pp[1]
    mul_of_min_and_sum = max(mul_of_min_and_sum, pp[0] * acc)
print(mul_of_min_and_sum)