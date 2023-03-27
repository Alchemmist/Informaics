a = input()
is_palind = True
for i in range(len(a) // 2):
    if a[i] != a[-(i + 1)]:
        is_palind = False
print("YES" if is_palind else "NO")
