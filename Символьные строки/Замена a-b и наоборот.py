a = input()
b = ''
count = 0
for i in a:
    if i == 'a':
        b += 'b'
        count += 1
    elif i == 'A':
        b += 'B'
        count += 1
    elif i == 'b':
        b += 'a'
        count += 1
    elif i == 'B':
        b += 'A'
        count += 1
    else:
        b += i

print(b)
print(count)
