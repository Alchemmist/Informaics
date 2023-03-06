with open('input.txt', mode='r', encoding='utf-8') as file:
    numbers = [i for i in map(int, file.readlines()) if i == numbers[-1] and i % 2 == 0]

with open('output.txt', mode='w', encoding='utf-8') as file:
    if numbers:
        file.write(f'{min(numbers)} {max(numbers)}')
    else:
        file.write(f'0')
