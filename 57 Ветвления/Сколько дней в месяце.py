seasons = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
    12: 30,

}
exec("try:print(seasons[int(input())])\nexcept KeyError:print('0')")