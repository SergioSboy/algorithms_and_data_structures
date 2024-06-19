MAX = 1000010

h = [0] * MAX


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    heights = list(map(int, data[1:n + 1]))

    res = 0

    for i in range(n):
        left = right = i

        while left > 0 and heights[left - 1] >= heights[i]:
            left -= 1
        while right < n - 1 and heights[right + 1] >= heights[i]:
            right += 1

        area = (right - left + 1) * heights[i]
        if area > res:
            res = area

    print(res)


if __name__ == "__main__":
    main()