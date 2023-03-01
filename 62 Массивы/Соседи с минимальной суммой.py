import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
last_num = random_nums[0]
summ = float('inf')

for ind, num in enumerate(random_nums[:-1]):
    if num + random_nums[ind + 1] <= summ:
        result = (ind, ind + 1)
        summ = num + random_nums[ind + 1]

print(result[0] + 1, result[1] + 1)
