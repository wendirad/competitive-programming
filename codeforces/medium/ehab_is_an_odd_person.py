n = int(input())

nums = list(map(int, input().split()))
f = True

e = 0
o = 0
for i in nums:
    if i % 2 == 1:
        o += 1
    else:
        e += 1

    if e > 0 and o > 0:
        print(*sorted(nums))
        f = False
        break

if f:
    print(*nums)
