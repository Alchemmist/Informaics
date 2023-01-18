x, y = map(float, input().split())
print('YES' if (x ** 2 + y ** 2 < 1) and not(y < -x and y > x) else 'NO')
