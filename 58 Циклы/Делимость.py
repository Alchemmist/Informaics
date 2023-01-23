a, b = map(int, input().split())
for i in range(a, b + 1):
    if '0' in str(i):
        continue
    count = 0
    for j in str(i):
        if i % int(j) == 0:
            count += 1
    if count == len(str(i)):
        print(i)
