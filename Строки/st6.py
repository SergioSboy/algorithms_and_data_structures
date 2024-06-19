def prefix_function(s):
    n = len(s)
    prefix = [0] * n
    prefix[0] = 0

    for i in range(1, n):
        j = prefix[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j

    return prefix


def kmp(pattern, text):
    p_size = len(pattern)
    t_size = len(text)
    prefix = prefix_function(pattern + "#" + text)
    res = []

    for i in range(p_size, p_size + 1 + t_size):
        if prefix[i] == p_size:
            res.append(i - p_size * 2 + 1)

    return res


if __name__ == "__main__":
    p = input()
    t = input()
    res = kmp(p, t)

    print(len(res))
    for i in res:
        print(i, end=" ")
