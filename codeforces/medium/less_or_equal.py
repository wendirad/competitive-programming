from collections import defaultdict, Counter
n, k = map(int, input().split())

nums = list(map(int, input().split()))


nums.sort()
if k < 1:
    if nums[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n:
    print(nums[-1])
else:
    bc = Counter(nums[:k])
    ac = Counter(nums[k:])
    el = nums[k-1]

    if ac[el] != 0:
        print(-1)
    else:
        print(el)
