"""Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.
"""

N_people = 10
K_slogov = 15
first_out = 0
new_list = []
for i in range(1, N_people + 1):
    new_list.append(i)
print("Первоначальный список", new_list)

while True:
    if len(new_list) == 1:
        print(f'Победил: {new_list[0]}')
        break
    else:
        if K_slogov > N_people:
            del_people = K_slogov - N_people - 1 + first_out
            if del_people >= len(new_list):
                while del_people >= len(new_list):
                    del_people = del_people - len(new_list)
        else:
            del_people = K_slogov - 1 + first_out
            while len(new_list) <= del_people:
                del_people = del_people - len(new_list)
        del new_list[del_people]
        first_out = del_people
        if first_out > len(new_list):
            first_out = first_out - len(new_list) - 1
        print(new_list)
