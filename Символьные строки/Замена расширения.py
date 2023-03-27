a = input().split('.')
extenc = input()
if len(a) == 1:
    print(f'{a}.{extenc}')
    exit()
a[-1] = extenc
print('.'.join(a))
