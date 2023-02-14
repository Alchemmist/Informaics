import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
count = 0
for num in random_nums:
    if (num // 10) % 2 == 0:
        count += 1
print(count)
