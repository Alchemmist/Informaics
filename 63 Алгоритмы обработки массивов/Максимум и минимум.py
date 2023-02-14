_ = int(input())
nums = list(map(int, input().split()))
print(*(min(a := [i for i in nums if i > 0 and i % 2 == 0]), max(a)) if len([i for i in nums if i > 0 and i % 2 == 0]) > 0 else -1)
