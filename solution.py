import random
import datetime

# 1
zero_and_one = random.random()
one_and_ten = random.randint(1, 10)

# 2
random_month = random.randint(1, 13)
random_year = random.randint(1900, 2020)


def get_random_day_max(month, year):
    if month == 2:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    return 31


random_day = random.randint(1, get_random_day_max(random_month, random_year))

random_date = datetime.date(random_year, random_month, random_day)
