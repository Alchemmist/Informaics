x, y = map(float, input().split())
print('YES' if x ** 2 + y ** 2 < 1 or (x ** 2 + y ** 2 > 1 and 0 < y < 1 and 0 < x < 1) else 'NO')
