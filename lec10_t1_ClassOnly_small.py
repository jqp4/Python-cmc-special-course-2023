# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_ClassOnly


s = ["a", "b", "c", "d"]
SLOTS = [a + b + c + d for a in s for b in s for c in s for d in s]


class Singleton(type):
    _instance = None

    def __call__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__()
        return cls._instance


class Struct(metaclass=Singleton):
    __slots__ = SLOTS

    def __init__(self) -> None:
        for name in SLOTS:
            setattr(self, name, name)


from itertools import product
from collections import Counter

lst = [Struct() for i in range(10000)]
FIELDS = ["".join(q) for q in product(*(["abcd"] * 4))]
res = Counter(getattr(l, FIELDS[i % len(FIELDS)]) for i, l in enumerate(lst))
print(sorted(set(res.values())))
