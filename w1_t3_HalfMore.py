# ejudge: https://ejudge.cs.msu.ru/new-client?SID=208df897cc3594c3&action=139&prob_id=4
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_HalfMore


# Имеется большая последовательность объектов (неважно каких), допускающих
# операцию сравнения. Известно, что некоторых одинаковых объектов в
# последовательности больше половины. Требуется, не храня последовательности,
# выяснить, чему они равны (т. е. вывести пример такого объекта).
# Ввод построчный, последняя строка — пустая.

objs_map = {}
obj = input()

while obj:
    objs_map[obj] = objs_map.get(obj, 0) + 1
    obj = input()

print(eval(max(objs_map, key=objs_map.get)))
