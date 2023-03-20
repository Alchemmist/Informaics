with open('input.txt') as file:
    data = file.readlines()
    count = 0
    maxi = -float('inf')
    for ind, num1 in enumerate(data):
        if ind == len(data) - 1: break
        num1 = int(num1)
        num2 = int(data[ind + 1])
        if num2 % 3 == 0 or num1 % 3 == 0:
            count += 1
        if num2 + num1 > maxi:
            maxi = num2 + num1

print(count)
print(maxi)
