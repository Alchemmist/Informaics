def clear(a: str) -> str:
    for i in '.,:;!?':
        a = a.replace(i, '')
    return a


with open('input.txt', encoding='utf-8') as file:
    changing = file.readline().strip()
    image = file.readline().strip()
    data = file.readlines()


with open('output.txt', encoding='utf-8', mode='w') as f:
    for i in data:
        for j in i.strip().split():
            if clear(j) == changing:
                j = j.replace(changing, image)
            f.write(j)
            f.write(' ')
        f.write('\n')