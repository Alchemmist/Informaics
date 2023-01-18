x, y = map(float, input().split())
print('YES' if (y > x and y < 2 - (x ** 2)) or (y < 2 - (x ** 2) and 0 < y < x) else 'NO')
