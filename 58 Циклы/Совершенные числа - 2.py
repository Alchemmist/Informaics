def is_perfect(n: int) -> bool:
    result = False
    dels = []
    for i in range(2, int(n ** 0.5) + 1):
        del1= i #2
        del2 = n // i #14

        if n % del1 == 0:
            dels.append(del1)
        if n % del2 == 0:
            dels.append(del2)

    if len(dels) > 0:
        result = True
    return result


n = int(input())
nothing = True
for i in range(1, n + 1):
    if is_perfect(i):
        print(i)
        nothing = False

if nothing:
    print(0)

