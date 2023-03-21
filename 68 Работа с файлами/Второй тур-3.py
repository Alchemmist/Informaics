with open('input.txt', encoding='utf-8') as file:
    changing = file.readline().strip()
    image = file.readline().strip()
    data = file.readlines()


with open('output.txt', encoding='utf-8', mode='w') as f:
