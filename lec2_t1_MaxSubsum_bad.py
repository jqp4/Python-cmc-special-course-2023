# ejudge: https://ejudge.cs.msu.ru/new-client?SID=208df897cc3594c3&action=139&prob_id=2
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_MaxSubsum

# Ввести в столбик последовательность целых (положительных и отрицательных) чисел,
# не равных нулю; в конце этой последовательности стоит 0. Вывести наибольшую
# сумму последовательно идущих элементов этой последовательности (не менее одного).

flag = True
number = int(input())
max_sub_sum = number
sub_sum = 0

while number != 0:
    if flag and (number < 0):
        if number > max_sub_sum:
            max_sub_sum = number
    else:
        flag = False
        sub_sum += number
        if sub_sum > max_sub_sum:
            max_sub_sum = sub_sum
            
    if sub_sum < 0:
        sub_sum = 0
        flag = True

    number = int(input())

print(max_sub_sum)
