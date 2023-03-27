a = input()
b = ''
count = 0
for i in a:
    if i == 'a':
        b += 'b'
        count += 1
    else:
        b += i

print(b)
print(count)