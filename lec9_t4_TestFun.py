# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_TestFun


class Tester:
    def __init__(self, func):
        self.func = func

    def __call__(self, suite, allowed=()):
        result = 0

        for s in suite:
            try:
                self.func(*s)
            except tuple(allowed):
                result = -1
            except:
                return 1

        return result
