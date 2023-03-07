def sum_num(n: str) -> int:
    return sum([int(i) for i in n])


with open('input.txt', mode='r', encoding='utf-8') as file:
    nums = sorted(file.read().strip().splitlines(), reverse=True, key=sum_num)

with open('output.txt', mode='w', encoding='utf-8') as file:
    fin = "\n".join(nums)
    file.write(f'{fin}')
