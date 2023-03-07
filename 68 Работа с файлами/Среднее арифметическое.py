summ = 0
count = 0
with open('input.txt', mode='r', encoding='utf-8') as file:
    n = file.readline().strip()
    while n:
        summ += int(n)
        count += 1
        n = file.readline().strip()


with open('output.txt', mode='w', encoding='utf-8') as file:
    file.write(f'{(summ / count):.3f}')

