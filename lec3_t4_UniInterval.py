# ejudge: https://ejudge.cs.msu.ru/new-client?SID=9ecef12f1bb88dbe&action=139&prob_id=9
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_UniInterval

# Объединение отрезков

# Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой. Рассмотрим объединение этих отрезков
# и найдём длину этого объединения (т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).

# Пример:
# >>> (66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)
# >>> 213

# Объяснение:
# Здесь имеются три группы накладывающихся отрезков:
# ((18, 58), (21, 81), (66, 91)),
# ((152, 230), (158, 211), (183, 236)) и
# ((286, 332), (294, 330), (323, 342)).
# Их длины 91 - 18 + 236 - 152 + 342 - 286 = 213

# Линейный алгоритм O(N log N): https://e-maxx.ru/algo/length_of_segments_union
# Положим все координаты концов отрезков в массив X и отсортируем его по значению координаты.
# Дополнительное условие при сортировке - при равенстве координат первыми должны идти левые концы.
# Кроме того, для каждого элемента массива будем хранить, относится он к левому или к правому концу отрезка.
# Теперь пройдёмся по всему массиву, имея счётчик C перекрывающихся отрезков. Если C отлично от нуля, то к результату
# добавляем разницу Xi - Xi-1. Если текущий элемент относится к левому концу, то увеличиваем счётчик C, иначе уменьшаем его.


allSegments = eval(input())
data = []

for segment in allSegments:
    data.append((segment[0], False))
    data.append((segment[1], True))

data.sort(key=lambda x: x[0])

length = 0
counter = 0

for i in range(len(data)):
    if counter != 0 and i != 0:
        length += data[i][0] - data[i - 1][0]
    if data[i][1]:
        counter += 1
    else:
        counter -= 1

if length < 0:
    length *= -1

print(length)