import calendar


try:
    num_days = calendar.monthrange(2023, int(input()))[1]
    print(num_days)
except calendar.IllegalMonthError:
    print(0)
