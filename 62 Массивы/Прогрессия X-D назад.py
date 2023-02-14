x, d, n = map(int, input().split())
a = []
for i in range(x, n*d + x, d):
    a.append(i)
print(*a[::-1])
