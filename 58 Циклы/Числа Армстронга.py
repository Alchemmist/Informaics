a, b = map(int, input().split())
nothing = True
for i in range(a, b + 1):
    summ = 0
    for j in str(i):
        summ += int(j) ** len(str(i))
    if summ == i:
        print(i, end=' ')
        nothing = False
print(-1 if nothing else '')
