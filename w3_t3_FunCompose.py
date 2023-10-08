# ejudge: https://ejudge.cs.msu.ru/client?SID=0b72bb6a838388b3&action=139&prob_id=12
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_FunCompose

# Написать функцию (точнее, функционал) compose(f, g), которому на вход подаётся два объекта-функции: 
# f(x, y) от двух параметров, и g(x₁, …, xₙ) от произвольного количества параметров. 
# compose(f, g) должна возвращать функцию h() от n параметров, являющуюся результатом применения 
# f() к g(x₁, …, xₙ) (в прямом порядке) и g(xₙ, …, x₁) (в обратном порядке)


# def compose_old(f, g):
#     def h(*args):
#         return f(g(*args), g(*args[::-1]))
#     return h


compose = lambda f, g: lambda *args: f(g(*args), g(*args[::-1]))


# from math import *
# print(compose(max, pow)(5, 6))
