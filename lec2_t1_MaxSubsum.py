# ejudge: https://ejudge.cs.msu.ru/new-client?SID=208df897cc3594c3&action=139&prob_id=2
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_MaxSubsum

# Ввести в столбик последовательность целых (положительных и отрицательных) чисел,
# не равных нулю; в конце этой последовательности стоит 0. Вывести наибольшую
# сумму последовательно идущих элементов этой последовательности (не менее одного).

# если есть отрезок с положительной суммой N, за которым следует отрезок с отрицательной
# суммой -K, по модулю меньшей N (|K|<N), а за ним следует отрезок с положительной суммой M,
# то все три отрезка дадут сумму N-K+M большую N и M. Обратно, если |K|>N, то N-K+M ни при
# каких условиях не превзойдёт M.
#
# Так что мы просто считаем текущую сумму всех элементов, запоминая, когда она принимала
# наибольшее значение, а если текущая сумма падает ниже 0, дожидаемся положительного числа,
# чтобы начать считать её заново.

number = int(input())
max_sub_sum = number
sub_sum = number if number > 0 else 0

number = int(input())

while number != 0:
    if number < 0 and number > max_sub_sum:
        max_sub_sum = number
        sub_sum = 0
    else:
        sub_sum += number
        if sub_sum < 0:
            sub_sum = 0
        else:
            if sub_sum > max_sub_sum:
                max_sub_sum = sub_sum

    number = int(input())

print(max_sub_sum)
