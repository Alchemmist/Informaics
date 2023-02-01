a = int(input())
nums = []
while a != 0:
    nums.append(a)
    a = int(input())
print(min(nums), max(nums))
