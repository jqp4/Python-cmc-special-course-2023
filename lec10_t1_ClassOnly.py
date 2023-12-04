# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_ClassOnly


def slotsGenerator():
    chars = ["a", "b", "c", "d"]
    for c1 in chars:
        for c2 in chars:
            for c3 in chars:
                for c4 in chars:
                    yield c1 + c2 + c3 + c4


SLOTS = list(slotsGenerator())


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Value:
    __slots__ = "index"

    def __init__(self, index) -> None:
        self.index = index

    def __str__(self) -> str:
        return SLOTS[self.index]


class Struct(metaclass=Singleton):
    __slots__ = SLOTS

    def __init__(self) -> None:
        for index, name in enumerate(SLOTS):
            setattr(self, name, Value(index))
