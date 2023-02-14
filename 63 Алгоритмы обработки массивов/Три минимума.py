_, nums = int(input()), list(map(int, input().split()))
nums.sort()
print(*nums[0:3])
