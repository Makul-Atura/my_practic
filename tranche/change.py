import datetime


def get_correct_date_format(input_str):
    result = datetime.date(
        int(input_str[6:10]), int(input_str[3:5]), int(input_str[0:2])
    )

    return result
