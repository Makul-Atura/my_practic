import datetime


def get_correct_date(input_str):
    result = datetime.date(
        int(input_str[6:10]), int(input_str[3:5]), int(input_str[0:2])
    )

    return result


def calc_year_days(start_date, end_date):
    diff = end_date.year - start_date.year

    if diff == 1:
        result = (end_date - start_date).days
        return result
    elif diff > 1:
        for num in range(1, diff + 1):
            next_year = datetime.date(
                start_date.year + num,
                start_date.month,
                start_date.day
            )

            result = (next_year - start_date).days
            print(result)


x = datetime.date(2020, 1, 1)
y = datetime.date(2022, 1, 1)
print(calc_year_days(x, y))
