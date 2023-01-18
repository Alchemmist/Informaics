x, y = map(float, input().split())
print('YES' if (x ** 2 + y ** 2 < 1 and x > 0) or (x - 1 < y < 1 and x > 0) else 'NO')
