n = int(input())
a, b = 1, 1
nums = []
for i in range(1, n + 1):
    nums.append(a)
    a, b = b, a + b

print(*nums)
