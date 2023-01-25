a, b = map(int, input().split())
nothing = True
for i in range(a, b + 1):
    if str(i) == str(i ** 2)[len(str(i ** 2)) - len(str(i)):]:
        print(i, end=' ')
        nothing = False
print(-1 if nothing else '')
