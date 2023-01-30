n = int(input())
check = True
s = 0
while s < n:
    n -= 1
    if n % 2 == 0 and n > 0:
        print(2 ** n, end=' ')
        check = False
if check:
    print(0)

