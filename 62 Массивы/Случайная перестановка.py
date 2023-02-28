import random


n = int(input())
result = [i for i in range(1, n + 1)]
random.shuffle(result)
print(*result)
