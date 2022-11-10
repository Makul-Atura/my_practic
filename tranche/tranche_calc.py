import datetime
import change


def get_days_amount_1(date_1, date_2, date_3, date_4):
    year_days =1
    days_of_1_per = (date_2 - date_1).days
    days_of_2_per = (date_4 - date_3).days

    return days_of_1_per / 365, days_of_2_per / 365


def calculation_1(koeff_1, koeff_2, summ, days_amount_1, days_amount_2):
    x_1 = summ * days_amount_1 * (koeff_1 / 100)
    x_2 = summ * days_amount_2 * (koeff_2 / 100)
    x = x_1 + x_2

    return x


def get_days_amount_2(date_1, date_2):
    date_1 = date_1.split('.')
    date_2 = date_2.split('.')
    cur_t_1 = datetime.date(int(date_1[2]), int(date_1[1]), int(date_1[0]))
    cur_t_2 = datetime.date(int(date_2[2]), int(date_2[1]), int(date_2[0]))

    return (cur_t_2 - cur_t_1).days / 365


def calculation_2(koeff, summ, days_amount):
    x = summ * days_amount * (koeff / 100)

    return x


p = int(input('Введите сумму транша в рублях: '))
k_amount = int(input('Введите кол-во периодов: '))

if k_amount == 2:
    receipt_date = input('Введите дату поступления на счет (дд.мм.гггг): ')
    receipt_date = change.get_correct_date_format(receipt_date)
    end_date_1 = input(f'Введите дату окончания 1-го перода ('
                 f'дд.мм.гггг): ')
    end_date_1 = change.get_correct_date_format(end_date_1)
    end_date_2 = input(f'Введите дату начала 2-го периода ('
                 f'дд.мм.гггг): ')
    end_date_2 = change.get_correct_date_format(end_date_2)
    return_date = input('Введите дату возврата (дд.мм.гггг): ')
    return_date = change.get_correct_date_format(return_date)

    days_1, days_2 = get_days_amount_1(
        receipt_date,
        end_date_1,
        end_date_2,
        return_date
    )
    k_1 = int(input('Введите 1-ю процентную ставку: '))
    k_2 = int(input('Введите 2-ю процентную ставку: '))
    result = calculation_1(k_1, k_2, p, days_1, days_2)
# else:
#     t_1 = input('Введите дату поступления на счет (дд.мм.гггг): ')
#     t_2 = input('Введите дату возврата (дд.мм.гггг): ')
#     days = get_days_amount_2(t_1, t_2)
#     k = int(input('Введите процентную ставку: '))
#     result = calculation_2(k, p, days)
#
# print('\nОбщее начисление:', round(result, 2))
