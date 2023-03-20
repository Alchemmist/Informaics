def vur(a: list[int, int, int]) -> bool:


with open('b.txt') as f:
    count = 0
    for i in f.readlines():
        i = i.strip()
        a = list(map(int, i.split()))
        check = 0
        for l in a:
            if ind == len(a) - 2: break
            if vur([j, a[ind + 1], a[ind + 2]]):
                check += 1
print(count)
