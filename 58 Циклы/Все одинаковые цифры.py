a = input()
early = a[0]
for i in a:
    if i != early:
        print('NO')
        exit()
    early = i
print('YES')
