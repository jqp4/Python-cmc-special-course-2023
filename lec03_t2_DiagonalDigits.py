# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_DiagonalDigits

# Цифры по диагонали

# Ввести целые M и N (0 ⩽ M, N ⩽ 1000), вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 …
# в виде прямоугольной матрицы N×M, заполненной из верхнего левого угла по следующему правилу:

# 1. На каждом шаге заполняется очередная диагональ матрицы с одинаковой суммой координат
# 2. Диагонали заполняются поочерёдно сверху вниз и снизу вверх (таким образом формируется
#   непрерывный «путь» из верхнего левого угла в правый нижний)

# Данные в этой задаче удобно хранить в виде списка списков

# Пример:
# 6, 5

# 0 2 3 9 0 9
# 1 4 8 1 8 0
# 5 7 2 7 1 6
# 6 3 6 2 5 7
# 4 5 3 4 8 9


M, N = eval(input())
matrix = [[0 for _ in range(M)] for _ in range(N)]
counter = 1
i = 0
j = 0

while counter < M * N:
    if j == M - 1:
        i += 1
    elif i == N - 1:
        j += 1
    elif j == 0:
        i += 1
    elif i == 0:
        j += 1

    done = False
    goingUp = j == 0 or i == N - 1

    while not done:
        matrix[i][j] = counter % 10
        counter += 1

        if goingUp:
            if i > 0 and j < M - 1:
                i -= 1
                j += 1
            else:
                done = True
        else:
            if i < N - 1 and j > 0:
                i += 1
                j -= 1
            else:
                done = True

for i in range(0, N):
    for j in range(0, M):
        print(matrix[i][j], end=" ")
    print()
