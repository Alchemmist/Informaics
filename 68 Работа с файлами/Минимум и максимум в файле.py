minn = float('inf')
maxx = -float('inf')

with open('input.txt', mode='r', encoding='utf-8') as file:
    n = file.readline().strip()
    while n:
        if int(n) > 0 and int(n) % 2 == 0:
            if int(n) > maxx: maxx = int(n)
            if int(n) < minn: minn = int(n)
        n = file.readline().strip()


with open('output.txt', mode='w', encoding='utf-8') as file:
    if maxx == -float('inf'):
        file.write(f'0')
    else:
        file.write(f'{minn} {maxx}')

