x, n = map(int, input().split())
a = []
for i in range(n + x - 1, x - 1, -1):
    a.append(i)

print(*a)
