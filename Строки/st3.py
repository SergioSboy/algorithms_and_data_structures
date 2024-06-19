def calc_hash(s, P, M):
    H = [0] * (len(s) + 1)
    power = [1] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        H[i] = (H[i - 1] * P + ord(s[i - 1])) % M
        power[i] = (power[i - 1] * P) % M
    return H, power


def hash(H, power, L, R, P, M):
    return (H[R] - H[L - 1] * power[R - L + 1] + M * M) % M


P = 26
M = 10 ** 9 + 9

a = input()
b = input()

H_a, power = calc_hash(a, P, M)
H_b, _ = calc_hash(b + b, P, M)

count = 0
l = set([hash(H_b, power, i + 1, i + len(b), P, M) for i in range(len(b))])

for start in range(len(a) - len(b) + 1):
    if hash(H_a, power, start + 1, start + len(b), P, M) in l:
        count += 1

print(count)
