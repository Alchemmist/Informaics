with open('a.txt', encoding='utf-8-sig') as f:
    count = 0

    for i in f.readlines():
        i = i.strip()
        a = list(map(int, i.split()))
        for ind, j in enumerate(a):
            if ind == len(a) - 1: break
            if (j + a[ind + 1]) in a:
                count += 1
print(count)
