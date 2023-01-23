a, b = map(int, input().split())
c, d = map(int, input().split())
nothing = True
for i in range(10000, 99999):
    if i % a == b and i % c == d:
        print(i, end=' ')
        nothing = False
if nothing:
    print(-1)
    