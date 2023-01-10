month, day = map(int, input().split())
m1 = (month - 1)
print(365 - ((m1 * 31) + (m1 * 30) + day))
