with open('input.txt', mode='r', encoding='utf-8') as file:
    numbers = list(map(int, file.readlines()))

with open('output.txt', mode='w', encoding='utf-8') as file:
    if numbers:
        file.write(f'{(sum(numbers) / len(numbers)):.3f}')
    else:
        file.write(f'0')
