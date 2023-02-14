_, nums = int(input()), list(map(int, input().split()))
count = 0
finish = []
for i in range(len(nums)):
    if nums[i] != nums[i + 1]:
        finish.append(count)
        count = 0
    count += 1
print(max(finish))