n = int(input())
nums = list(map(int, input().split()))
x = int(input())

print(*[ind + 1 for ind, num in enumerate(nums) if num == x])
