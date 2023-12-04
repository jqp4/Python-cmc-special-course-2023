# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_EvalFormulae


import re


def evalform(formula, *args):
    var_set = set(filter(None, re.split("[^a-zA-Z]+", formula)))
    var_value_map = dict(zip(sorted(list(var_set)), args))
    return eval(formula, var_value_map)


# print(evalform("b*2 + a*3 + b//3 + c", 11, 3, 2))
