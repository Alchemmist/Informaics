n = int(input())
nums = list(map(int, input().split()))

print(*[ind + 1 for ind, num in enumerate(nums) if num == min(nums)])
