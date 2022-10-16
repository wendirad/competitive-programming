    import math
    n, m, a = map(int, input().split())
    print(int(math.ceil(n / a) * math.ceil(m / a)))