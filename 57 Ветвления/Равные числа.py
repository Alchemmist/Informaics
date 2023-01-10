finish = 0
a = input().split()
for i in a:
    finish = a.count(i) if a.count(i) - 1 > finish else finish
print(finish)
