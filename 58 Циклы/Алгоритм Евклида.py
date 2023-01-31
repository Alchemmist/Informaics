a, b = sorted(list(map(int, input().split())), reverse=True)
iters = 0
while a != b:
    a -= b
    iters += 1

print(a, iters)
