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
    el = nums[k - 1]
    if nums[k] == el:
        print(-1)
    else:
        print(el)
