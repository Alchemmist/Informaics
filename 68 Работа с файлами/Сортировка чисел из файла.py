with open('input.txt', mode='r', encoding='utf-8') as file:
    nums = sorted(file.read().strip().splitlines(), reverse=True, key=lambda x: int(x))

with open('output.txt', mode='w', encoding='utf-8') as file:
    fin = "\n".join(nums)
    file.write(f'{fin}')
