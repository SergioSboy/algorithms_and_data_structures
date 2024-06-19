def can_split(nums, k, max_sum):
    count = 1
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum > max_sum:
            count += 1
            curr_sum = num
    return count <= k


def split_array(nums, k):
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if can_split(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left


n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(split_array(nums, k))
