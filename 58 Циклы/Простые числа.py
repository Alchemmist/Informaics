a, b = map(int, input().split())
nothing = True
for i in range(a, b + 1):
    is_prime = True
    for n in range(2, int(i ** 0.5) + 1):
        if i % n == 0:
            is_prime = False
            break

    if is_prime:
        print(i, end=' ')
        nothing = False
print(0 if nothing else '')
