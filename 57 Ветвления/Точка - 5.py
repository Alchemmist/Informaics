x, y = map(float, input().split())
print('YES' if (y > x or (y < x and x < 0)) and (x ** 2 + y ** 2 < 1) else 'NO')
