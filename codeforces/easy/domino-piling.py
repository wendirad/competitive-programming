M, N = map(int, input().split())

fair_valid = int(M / 2) * N

sides = (M % 2) * int(N / 2)

print(fair_valid + sides)