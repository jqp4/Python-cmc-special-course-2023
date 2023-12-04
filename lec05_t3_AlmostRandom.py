# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_AlmostRandom

import random


def divrandom(a, b, s, p):
    if a > b:
        a, b = b, a

    if s % p == 0 and a % p == 0:
        return 0

    answer = 0
    N = (b - a + s) // s

    while answer % p == 0:
        answer = a + random.randrange(N) * s

    return answer


# print("answer:", divrandom(10, 21, 5, 2))

# m = {}

# for _ in range(10000):
#     a = divrandom(-1000, 1000, 2, 7)
#     if a in m:
#         m[a] += 1
#     else:
#         m[a] = 1

# for a, count in m.items():
#     print(f"{a:3}: {count}")

# L, D = 20000, 1000
# S = abs(sum(divrandom(-1000, 1000, 2, 7) for i in range(L)))
# print("OK" if S / (L * D) < 0.01 else "Sum is too large: {S}")
