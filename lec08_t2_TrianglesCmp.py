# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_TrianglesCmp

from math import sqrt, isclose

# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=


class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

        if not (
            self.a > 0
            and self.b > 0
            and self.c > 0
            and self.a + self.b > self.c
            and self.a + self.c > self.b
            and self.b + self.c > self.a
        ):
            self.area = 0
            return

        p = (self.a + self.b + self.c) / 2
        self.area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def __bool__(self) -> bool:
        return self.area != 0

    def __str__(self) -> str:
        return f"{self.a}:{self.b}:{self.c}"

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Triangle):
            raise TypeError()

        if isclose(self.a, __value.a):
            if isclose(self.b, __value.b) and isclose(self.c, __value.c):
                return True
            if isclose(self.b, __value.c) and isclose(self.c, __value.b):
                return True

        if isclose(self.b, __value.b):
            if isclose(self.a, __value.a) and isclose(self.c, __value.c):
                return True
            if isclose(self.a, __value.c) and isclose(self.c, __value.a):
                return True

        if isclose(self.c, __value.c):
            if isclose(self.a, __value.a) and isclose(self.b, __value.b):
                return True
            if isclose(self.a, __value.b) and isclose(self.b, __value.a):
                return True

        if isclose(self.a, __value.b):
            if isclose(self.b, __value.c) and isclose(self.c, __value.a):
                return True

        if isclose(self.a, __value.c):
            if isclose(self.b, __value.a) and isclose(self.c, __value.b):
                return True

        return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Triangle):
            raise TypeError()

        return self.area < __value.area

    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Triangle):
            raise TypeError()

        return self.area <= __value.area

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Triangle):
            raise TypeError()

        return self.area > __value.area

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Triangle):
            raise TypeError()

        return self.area >= __value.area


abs = lambda triangle: triangle.area


# # test 1

# tri = (
#     Triangle(3, 4, 5),
#     Triangle(5, 4, 3),
#     Triangle(7, 1, 1),
#     Triangle(5, 5, 5),
#     Triangle(7, 4, 4),
# )

# for a, b in zip(tri[:-1], tri[1:]):
#     print(a if a else b)
#     print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
#     print(a == b)
#     print(a >= b)
#     print(a < b)

# # test 2

# N = 6
# tri = [Triangle(i/2, j/2, k/2) for i in range(1, N) for j in range(1, N) for k in range(1, N)]
# print(sum(abs(t) for t in tri))
# print(sum(t1 == t2 for t1 in tri for t2 in tri))
# print(sum(t1 < t2 for t1 in tri for t2 in tri))
# print(sum(t1 >= t2 for t1 in tri for t2 in tri))

# # test 3

# N = 8
# tri = [Triangle(i/2, j/2, k/2) for i in range(1, N) for j in range(1, N) for k in range(1, N)]
# print(sum(abs(t) for t in tri))
# print(sum(t1 == t2 for t1 in tri for t2 in tri))
# print(sum(t1 < t2 for t1 in tri for t2 in tri))
# print(sum(t1 >= t2 for t1 in tri for t2 in tri))
