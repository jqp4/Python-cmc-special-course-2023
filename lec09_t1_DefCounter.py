# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_DefCounter

# перегрузка операторов - https://pythonworld.ru/osnovy/peregruzka-operatorov.html


from collections import Counter


class DefCounter(Counter):
    def __init__(*args, missing=-1, **kwds):
        self, *args = args
        self.missing = missing
        super(Counter, self).__init__()
        self.update(*args, **kwds)

    def __missing__(self, key):
        return self.missing

    # Version 3.10: AttributeError: 'Counter' object has no attribute 'total'
    def total(self):
        return sum(self.values())

    def __abs__(self):
        return sum(x for x in self.values() if x > 0)


# A = DefCounter("QWEqweQWEqweQWE", missing=-10)
# print(A)
# A["P"] += 5
# print(A["T"], A["P"], abs(A), A.total())
# print(A)
