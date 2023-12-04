# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_Det4x4

# Матрица 4×4 задаётся кортежем из 4 кортежей по 4 целых числа в каждом. Написать функцию 
# det4(r0, r1, r2, r3), вычисляющую точный определитель матрицы (r0, r1, r2, r3). 
# Пользоваться itertools нельзя. Числа содержат не более 66666 десятичных знаков.


def minor(matrix, k):
    res = []
    for r in matrix[1:]:
        row = []
        for j in range(len(r)):
            if j != k:
                row.append(r[j])
        res.append(row)
    return res


def det4(*matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det = 0
    for i in range(n):
        det += (-1) ** i * matrix[0][i] * det4(*minor(matrix, i))
    return det


# print(det4((5, -4, 4, -7), (1, -2, 6, 0), (3, -8, -6, -4), (-1, 2, -9, 3)))
