import random


a, b, n = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
maxi = -1
for num in random_nums:
    if num > maxi and num % 2 == 0 and num != 0:
        maxi = num
print(maxi)
