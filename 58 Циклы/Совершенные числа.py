n = int(input())
dels = []
for i in range(2, int(n ** 0.5) + 1):
    del1= i #2
    del2 = n // i #14

    if n % del1 == 0:
        dels.append(del1)
    if n % del2 == 0:
        dels.append(del2)

if len(dels) > 0 and sum(dels) + 1 == n:
    dels.sort()
    print(1, *dels)
else:
    print(0)

