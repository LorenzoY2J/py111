"""Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
(час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
(т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день
"""

list_order = [(1, 3), (7, 9), (5, 6), (4, 2), (8, 10)]
new_list = []


def rockets(list_order, new_list):
    rocket = True
    for first_rocket in list_order:
        start_time = first_rocket[0]
        finish_time = first_rocket[1]
        time = range(start_time, finish_time)
        for second_rocket in list_order:
            if first_rocket == second_rocket or second_rocket in new_list:
                pass
            else:
                if second_rocket[0] == start_time:
                    rocket = False
                if second_rocket[1] in time:
                    rocket = False
                if second_rocket[0] in time:
                    rocket = False
                if start_time in range(second_rocket[0], second_rocket[1] + 1):
                    rocket = False
        new_list.append(first_rocket)

    if rocket:
        print('Достаточно первой ракеты')
    else:
        print('Не достаточно первой ракеты')


rockets(list_order, new_list)
