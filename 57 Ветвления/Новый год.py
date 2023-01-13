import calendar


def get_day_by_month(month_number: int) -> int:
    num_days = calendar.monthrange(2023, month_number)[1]
    return num_days


month, day = map(int, input().split())
if month < 0 or month > 12 or day > 31 or day < 0:
    print(-1)
    exit()

diff = 365 - day
for i in range(1, month):
    diff -= get_day_by_month(i)
print(diff if diff != 0 else '365')
