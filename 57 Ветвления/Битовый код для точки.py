x, y = map(float, input().split())

print(1 if y < 1 else 0, end='')
print(1 if y < -x else 0, end='')
print(1 if -1 < y < 1 and -1 < x < 1 else 0, end='')
print(1 if -1 < y < 1 and 0 < x < 2 else 0)
