a, b = map(int, input().split())
finish = 0
for i in range(a, b + 1):
    finish += i ** 2
print(finish)
