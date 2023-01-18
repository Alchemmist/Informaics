x, y = map(float, input().split())
print('YES' if (y > 1 - x and y > 2 * x ** 2 and x < 1) or (0 < x < 1 and y > 1 - x and y < 2 * x**2) else 'NO')
