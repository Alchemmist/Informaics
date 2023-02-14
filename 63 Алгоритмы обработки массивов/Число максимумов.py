n = int(input())
nums = list(map(int, input().split()))

print(a := max(nums), len([i for i in nums if i == a]))
