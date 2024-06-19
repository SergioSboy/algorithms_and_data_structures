def max1(a, b):
    if len(a) >= len(b):
        return a
    return b

def main():
    s = input().strip()
    L = len(s)
    d = [[""] * 101 for _ in range(101)]

    for i in range(L):
        d[i][i] = s[i]

    for i in range(1, L):
        for j in range(i, L):
            g = j - i
            if s[g] != s[j]:
                d[g][j] = max1(d[g][j - 1], d[g + 1][j])
            else:
                d[g][j] = max1(d[g][j - 1], max1(d[g + 1][j], s[g] + d[g + 1][j - 1] + s[j]))

    print(len(d[0][L - 1]))
    print(d[0][L - 1])

if __name__ == "__main__":
    main()
