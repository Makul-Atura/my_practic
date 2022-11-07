import datetime


def get_days_amount_1(date_1, date_2, date_3, date_4):
    date_1 = date_1.split('.')
    date_2 = date_2.split('.')
    date_3 = date_3.split('.')
    date_4 = date_4.split('.')
    cur_t_1 = datetime.date(int(date_1[2]), int(date_1[1]), int(date_1[0]))
    cur_t_2 = datetime.date(int(date_2[2]), int(date_2[1]), int(date_2[0]))
    cur_t_3 = datetime.date(int(date_3[2]), int(date_3[1]), int(date_3[0]))
    cur_t_4 = datetime.date(int(date_4[2]), int(date_4[1]), int(date_4[0]))

    return (cur_t_2 - cur_t_1).days / 360, (cur_t_4 - cur_t_3).days / 360


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

    return (cur_t_2 - cur_t_1).days / 360


def calculation_2(koeff, summ, days_amount):
    x = summ * days_amount * (koeff / 100)

    return x


p = int(input('Введите сумму транша в рублях: '))


k_amount = int(input('Введите кол-во периодов: '))

if k_amount == 2:
    t_1 = input('Введите дату поступления на счет (дд.мм.гггг): ')
    t_2 = input('Введите дату конца 1-го перода (дд.мм.гггг): ')
    t_3 = input('Введите дату начала 2-го периода (дд.мм.гггг): ')
    t_4 = input('Введите дату возврата (дд.мм.гггг): ')
    days_1, days_2 = get_days_amount_1(t_1, t_2, t_3, t_4)
    k_1 = int(input('Введите 1-ю процентную ставку: '))
    k_2 = int(input('Введите 2-ю процентную ставку: '))
    result = calculation_1(k_1, k_2, p, days_1, days_2)
else:
    t_1 = input('Введите дату поступления на счет (дд.мм.гггг): ')
    t_2 = input('Введите дату возврата (дд.мм.гггг): ')
    days = get_days_amount_2(t_1, t_2)
    k = int(input('Введите процентную ставку: '))
    result = calculation_2(k, p, days)

print('\nОбщее начисление:', round(result, 2))
