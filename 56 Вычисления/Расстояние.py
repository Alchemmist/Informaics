from math import sqrt


x1, y1= map(float, input().strip().split())
x2, y2= map(float, input().strip().split())
print(f'{(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)):.3f}')

