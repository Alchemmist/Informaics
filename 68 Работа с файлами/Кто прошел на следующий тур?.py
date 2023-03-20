with open('input.txt', encoding='utf-8') as file:
    k = int(file.readline())
    data = file.readlines()

with open('output.txt', encoding='utf-8', mode='w') as f:
    count = 0
    for i in data:
        surename, name, point = i.split()
        if int(point) > k:
            f.write(f'{count + 1}) {surename} {name}\n')
            count += 1
    f.write(f'{count}')
