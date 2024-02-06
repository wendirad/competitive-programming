t = int(input())

for test in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    if n == 1:
        print("YES")
        continue

    nums.sort()

    i = 1
    f = True
    while i < n:
        if abs(nums[i - 1] - nums[i]) > 1:
            print("NO")
            f = False
            break
        i += 1
    if f:
        print("YES")
