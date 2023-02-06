n = int(input())
dels = []
nothing = True
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        dels.append(i)
    if n % (i // n) == 0:
        dels.append(i // n)

if len(dels) > 1 and sum(dels) == n:
    print(*dels)
else:
    print(0)

