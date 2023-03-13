with open('input.txt', encoding='utf-8') as file:
    k = file.readline()
    for i in file.readlines():
        name, age, breed = i.split()