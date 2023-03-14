with open('input.txt', encoding='utf-8') as file:
    k = int(file.readline())
    data = file.readlines()

with open('output.txt', encoding='utf-8') as file:
    count = 0
    for i in data:
        name, age, breed = i.split()
        if int(age) < k:
            file.write(f'{name} {age} {breed}')
    file.write(f'{count}')