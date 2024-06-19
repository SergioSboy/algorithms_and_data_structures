def findNumberOfLIS(nums):
    ln = len(nums)
    longestExtensionList = [nums[0]]

    def binarySearchIdx(arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid
            else:
                return mid
        return right

    activeEnd = [{nums[0]: 1}]

    def numberSmallerThan(hashMap, target):
        deleteKeys = set()
        count = 0
        for key in hashMap:
            if key >= target:
                deleteKeys.add(key)
            else:
                count += hashMap[key]
        for key in deleteKeys:
            del hashMap[key]
        return count

    for i in range(1, ln):
        if nums[i] > longestExtensionList[-1]:
            extensionNumber = numberSmallerThan(activeEnd[-1], nums[i])
            longestExtensionList.append(nums[i])
            activeEnd.append({})
            activeEnd[-1][nums[i]] = extensionNumber
        elif nums[i] == longestExtensionList[-1]:
            extensionNumber = sum([activeEnd[-2][key] for key in activeEnd[-2]]) if len(activeEnd) > 1 else 1
            activeEnd[-1][nums[i]] += extensionNumber
        else:
            idx = binarySearchIdx(longestExtensionList, nums[i])
            longestExtensionList[idx] = nums[i]
            if idx > 0:
                n = numberSmallerThan(activeEnd[idx - 1], nums[i])
            else:
                n = 1
            if nums[i] not in activeEnd[idx]:
                activeEnd[idx][nums[i]] = n
            else:
                activeEnd[idx][nums[i]] += n
    return sum(activeEnd[-1].values())


n = int(input())

nums = list(map(int, input().split()))

print(findNumberOfLIS(nums) % (10 ** 9 + 7))
