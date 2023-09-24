# ejudge: https://ejudge.cs.msu.ru/new-client?SID=208df897cc3594c3&action=139&prob_id=3
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_SecondMax

# Ввести по одному в строке целые числа, не равные нулю (не менее одного,
# конец ввода — 0), вывести второй максимум последовательности (число,
# строго меньшее максимума последовательности, и не меньшее остальных
# чисел в ней), и NO, если такового нет.

number = int(input())

first_max = None
second_max = None

while number != 0:
    if first_max == None:
        first_max = number
    elif number > first_max:
        second_max = first_max
        first_max = number
    elif first_max > number and (second_max == None or number > second_max):
        second_max = number

    number = int(input())

if first_max != None and second_max != None and first_max > second_max:
    print(second_max)
else:
    print("NO")
