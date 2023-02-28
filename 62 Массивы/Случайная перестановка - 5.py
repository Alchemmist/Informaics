import random


n = int(input())
result = [i for i in range(1, n + 1)]
random.shuffle(result)
result[result.index(5)] = result[0]
result[0] = 5
print(*result)
