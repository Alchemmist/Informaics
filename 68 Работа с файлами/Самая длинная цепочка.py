count = 0
result = []

with open('input.txt', mode='r', encoding='utf-8') as file:
    n1 = file.readline().strip()
    while n1:
        n2 = file.readline().strip()
        if n2 == n1:
            count += 1
        else:
            result.append(count)
            count = 0
        n1 = n2


with open('output.txt', mode='w', encoding='utf-8') as file:
    file.write(f'{max(result) + 1}')