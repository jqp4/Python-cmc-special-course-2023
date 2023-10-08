# ejudge: https://ejudge.cs.msu.ru/client?SID=0b72bb6a838388b3&action=139&prob_id=10
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_ShefferStroke

# Написать функцию sheff(A, B), реализующую логическую операцию Штрих Шеффера A ↑ B по следующему принципу:
# * Если ровно один из операндов не пуст, возвращается этот операнд
# * Если оба операнда пусты, возвращается True
# * Если оба операнда непусты, возвращается False


# def sheff_old(a, b):
#     if a:
#         if b:
#             return False
#         return a
#     else:
#         if b:
#             return b
#         return True


sheff = lambda a, b: (False if b else a) if a else (b if b else True)


# print(sheff(1, 2))
# print(sheff([], 1.1))
# print(sheff((0, 0), ""))
