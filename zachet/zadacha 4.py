"""Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив), на которой определена стоимость захода
в каждую ячейку (все стоимости положительные). Необходимо найти путь минимальной стоимости из
заданной ячейки в заданную ячейку и вывести этот путь."""

massiv = [
    [3, 6, 7],
    [5, 2, 8],
    [7, 4, 1]
]


def search_min_way():
    coast = massiv.copy()
    coords = [(0, 0)]

    for j in range(1, len(coast[0])):
        coast[0][j] += coast[0][j - 1]

    for i in range(1, len(coast)):
        coast[i][0] += coast[i - 1][0]

    for i in range(1, len(coast)):
        for j in range(1, len(coast[0])):
            coast[i][j] += min(coast[i][j - 1], coast[i - 1][j])
            if coast[i][j - 1] <= coast[i - 1][j] and (i, j - 1) != coords[-1]:
                coords.append((i, j - 1))
            else:
                if (i - 1, j) != coords[-1]:
                    coords.append((i - 1, j))
    coords.append((len(coast) - 1, len(coast) - 1))

    print(coast[-1][-1])
    print(coords)


if __name__ == '__main__':
    search_min_way()
