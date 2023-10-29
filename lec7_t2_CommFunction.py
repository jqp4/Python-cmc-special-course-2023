# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_CommFunction


from itertools import permutations


def checkcomm(func, *args):
    is_first = True
    result = None

    for perm in permutations(args):
        if is_first:
            result = func(*perm)
            is_first = False
        else:
            if result != func(*perm):
                return False

    return True
