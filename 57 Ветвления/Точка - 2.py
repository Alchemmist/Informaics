from math import pi, sin

x, y = map(float, input().split())
print('YES' if 0 < y < 0.5 and 0 < x < pi and y < sin(x) else 'NO')
