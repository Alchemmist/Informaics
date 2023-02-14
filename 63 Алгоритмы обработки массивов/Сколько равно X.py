n = int(input())
nums = list(map(int, input().split()))
x = int(input())
print(len([i for i in nums if i == x]))
