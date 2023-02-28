import random


a, b, n, k = map(int, input().split())
random_nums = [random.randint(a, b) for _ in range(n)]
print(*random_nums)
count = 0
for num in random_nums:
    summ = 0
    for i in str(num):
        summ += int(i)
    if summ == k:
        count += 1
print(count)
