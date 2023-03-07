count = 0

with open('input.txt', mode='r', encoding='utf-8') as file:
    n1 = file.readline().strip()
    while n1:
        count += len(n1.split())
        n1 = file.readline().strip()


with open('output.txt', mode='w', encoding='utf-8') as file:
    file.write(f'{count}')
