"""
Ваша задача - посчитать суммарное количество шагов которое потребуется, чтобы подобрать все 3 предмета
 - ('C' - compass), ('M' - map), ('S' - spyglass), считая от вашей стартовой позиции.

Таким образом, итоговый результат будет суммой трех дистанций: от Y к C, от Y к M и от Y к S (не Y-C-M-S).
Учтите, что вы можете ходить в 8 направлениях - влево, вправо, вверх, вниз и по диагонали в любую сторону.
Ваша стартовая позиция - 'Y'.

navigation([['Y', 0, 0, 0, 'C'],
            [ 0,  0, 0, 0,  0],
            [ 0,  0, 0, 0,  0],
            ['M', 0, 0, 0, 'S']]) == 11 #4 шага от Y к C, 4 от Y к S и 3 от Y к M

т.е мы ищем минимальное количество шагов от точки где вы до точки где предмет, ходить можно как по
горизонтали/вертикали, так и по диагонали
"""


def navigation(matrix):
    i = 0
    for row in matrix:
        i += 1
        if 'Y' in row:
            coordinates_y = i, row.index('Y')

        if 'C' in row:
            coordinates_c = i, row.index('C')

        if 'M' in row:
            coordinates_m = i, row.index('M')

        if 'S' in row:
            coordinates_s = i, row.index('S')

    to_c = max(abs(coordinates_c[0] - coordinates_y[0]), abs(coordinates_c[1] - coordinates_y[1]))
    to_m = max(abs(coordinates_m[0] - coordinates_y[0]), abs(coordinates_m[1] - coordinates_y[1]))
    to_s = max(abs(coordinates_s[0] - coordinates_y[0]), abs(coordinates_s[1] - coordinates_y[1]))

    return f'{to_s + to_m + to_c}'

print(navigation([['Y', 0, 0, 0, 'C'], [ 0,  0, 0, 0,  0], [ 0,  0, 0, 0,  0], ['M', 0, 0, 0, 'S']]))