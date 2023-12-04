# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_MetaBool

DEBUG_MODE = False


def pprint(*args, **kwargs):
    if DEBUG_MODE:
        print(*args, **kwargs)


class empty(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwds):
        pprint("prepare", name, bases, kwds)
        return super().__prepare__(name, bases, **kwds)

    @staticmethod
    def __new__(metacls, name, parents, ns, **kwds):
        pprint("new", metacls, name, parents, ns, kwds)
        return super().__new__(metacls, name, parents, ns)

    def __init__(cls, name, parents, ns, **kwds):
        pprint("init", cls, parents, ns, kwds)

        def new_bool(self):
            for attr, value in self.__dict__.items():
                pprint(f"check {attr} = {value}")
                if not value:
                    pprint("empty attr!!!")
                    return False

            return True

        cls.__bool__ = new_bool
        return super().__init__(name, parents, ns)

    def __call__(cls, *args, **kwargs):
        pprint("\ncall", cls, args, kwargs)
        pprint(f"{cls.__name__}.__dict__ = {cls.__dict__}")
        return super().__call__(*args, **kwargs)
