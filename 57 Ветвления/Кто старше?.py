age = {key: int(value) for value, key in zip(input().split(), ['A', 'B', 'C'])}
print(*a if len(a := [key for key, value in age.items() if value >= max(age.values())]) < 3 else '0')
