result = ''
with open('input.txt', mode='r', encoding='utf-8') as file:
    n1 = file.readline().strip()
    while n1:
        s = ''
        for i in n1.split():
            if len(i) > len(s):
                s = i
        if len(s) > len(result):
            result = s
        n1 = file.readline().strip()


with open('output.txt', mode='w', encoding='utf-8') as file:
    file.write(f'{result}')
