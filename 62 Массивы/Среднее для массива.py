import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
maxi = -1
print(f'{(sum(random_nums) / len(random_nums)):.3f}')
