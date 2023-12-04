# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_SubString

from collections import UserString


class SubString(UserString):
    def __sub__(self, __value):
        other_string_data = None
        if isinstance(__value, self.__class__):
            other_string_data = __value.data
        elif isinstance(__value, str):
            other_string_data = __value
        else:
            return TypeError

        from collections import Counter

        result = []
        characters_to_delete = Counter(other_string_data)

        for char in self.data:
            if characters_to_delete.get(char, 0) > 0:
                characters_to_delete[char] -= 1
            else:
                result.append(char)

        return self.__class__("".join(result))


del UserString
