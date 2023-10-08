# ejudge: https://ejudge.cs.msu.ru/new-client?SID=208df897cc3594c3&action=139&prob_id=5
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_CubeSum

# Ввести натуральное число N и вывести, сколько ∃ различных пар натуральных чисел A и B:
# A³+B³=N (с точностью до перестановки). Вещественные операции (например, кубический корень)
# рекомендуется использовать как можно реже.

# Начнём с A=1, B=N**⅓. Если A³+B³ > N, будем уменьшать B на 1,
# в противном случае — увеличивать A на 1. Если равны, посчитаем это разложение.
# Как только A станет больше B, подсчёт закончим.

N = int(input())
counter = 0

A = 1
B = int(N ** (1 / 3)) + 1

while A <= B:
    S = A**3 + B**3

    if S > N:
        B -= 1
    elif S == N:
        # print(f"Pair: {A}, {B}")
        counter += 1
        A += 1
    else:
        A += 1

print(counter)
