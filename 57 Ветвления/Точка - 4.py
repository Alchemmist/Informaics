x, y = map(float, input().split())
print('YES' if y > x ** 2 - 2 and (y < -x or y < x) else 'NO')
