import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
random_nums2 = random_nums.copy()

