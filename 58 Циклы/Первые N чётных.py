nums = []
i = 0
a = int(input())
while len(nums) < a:
    if i > 0 and i % 2 == 0:
        nums.append(i)
    i += 1
print(*nums)
