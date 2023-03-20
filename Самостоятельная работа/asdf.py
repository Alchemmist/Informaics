with open('09.csv', encoding='utf-8-sig') as f:
    data = f.readlines()

count = 0
for i in data:
    a = sorted(map(int, i.strip().split(',')))
    repit = []
    not_repit = []
    for i in a:
        if a.count(i) >= 2:
            repit.append(i)
        else:
            not_repit.append(i)

    if (repit and not_repit) and (
        sum(not_repit) / len(not_repit) < sum(repit) / len(repit)
    ):
        count += 1
print(count)
