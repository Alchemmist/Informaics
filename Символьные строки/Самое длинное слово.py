a = input()
maxi = 0
result = ''
for i in a.split():
    if len(i) > maxi:
        result = i
        maxi = len(i)

print(result)
print(maxi)
