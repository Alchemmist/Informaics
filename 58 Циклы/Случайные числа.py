from random import randint

a, b, n = map(int, input().split())
for _ in range(n):
    print(randint(a, b), end=' ')
