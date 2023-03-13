with open('input.txt') as file:
    data = file.readlines()
    count = 0
    for i in data:
        nums = list(map(int, i.split()))
        count = 0
        repeat, not_repeat = [], []
        for i in nums:
            if nums.count(i) == 2:
                count += 1
            elif nums.count(i) == 1:
                not_repeat.append(i)
            else:
                repeat.append(i)

        if count != 2:
            check = False
        else:
            check = True


        if () and ():
            count += 1



print(count)
