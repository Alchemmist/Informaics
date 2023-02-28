import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
smal = []
big = []
for num in random_nums:
    if num < 50:
        smal.append(num)
    else:
        big.append(num)
if len(smal) == 0: smal.append(0)
if len(big) == 0: big.append(0)
print(f'{(sum(smal) / len(smal)):.3f} {(sum(big) / len(big)):.3f}')
