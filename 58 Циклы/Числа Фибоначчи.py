f1, f2 = 0, 1
n = int(input())
while f2 <= n:
    f2 = f1 + f2
    print(f1, end=' ')
    f1 = f2

