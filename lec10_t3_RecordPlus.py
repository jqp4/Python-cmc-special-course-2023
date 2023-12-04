# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_RecordPlus


def Record(s: str, **kwargs):
    def decorator(cls: object):
        # Составляем отсортированный список слотов для нового класса
        slots = set(cls.__slots__)
        slots.update(s.split())
        slots = list(slots)
        slots.sort()

        class Record(cls):
            __slots__ = slots

            # Генератор отсортированных имен атрибутов (__slots__ + readonly)
            def _attr_names_generator(self):
                attrs = [attr for attr in self.__dir__() if attr[0] != "_"]
                attrs.sort()

                for attr in attrs:
                    yield attr

            def __iter__(self):
                return self._attr_names_generator()

            def __str__(self):
                # Функция строчного представления атрибута типа "a=42"
                def get_attr_str(attr):
                    value = getattr(self, attr, None)
                    eq = lambda: "=" if attr in self.__slots__ else ":"
                    return f"{attr}{eq()}{value}" if value != None else attr

                return "|".join([get_attr_str(a) for a in self._attr_names_generator()])

        # Добавление readonly полей к классу
        for attr, value in kwargs.items():
            setattr(Record, attr, value)

        return Record

    return decorator


# @Record("b c", d=11, e=12)
# class C:
#     __slots__ = ["a", "b"]
#     c = 8
#     d = 9


# c = C()
# c.a, c.c = 42, 100500
# print(c, "//", "".join(c.__slots__))
# print(*(getattr(c, attr, "<NOPE>") for attr in c))
# for i, attr in enumerate(c):
#     try:
#         setattr(c, attr, i)
#     except AttributeError:
#         pass
# print(c, "//", *(getattr(c, attr, "<NOPE>") for attr in c))

# a=42|b|c=100500|d:11|e:12 // abc
# 42 <NOPE> 100500 11 12
# a=0|b=1|c=2|d:11|eл:12 // 0 1 2 11 12
