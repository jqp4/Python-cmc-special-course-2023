# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_EasyBnopnya

import sys

# Спойлер:  Если взять все символы из книги и попытаться составить словарь безошибочных
# перекодировок любой глубины, приводящих к различным результатам, он получится совсем небольшой
# (у меня вышло всего 265 вариантов); построение такого словаря на EJudge занимает около секунды.
# Перекодируем «Левин»-а во все эти варианты, ищем в предъявленном фрагменте, перекодируем по
# соответствующей схеме. Я бы ещё на всякий случай проверял, что после перекодировки встречаются
# только символы из книги. (необязательно) Сам я решал ещё тупее, если что ☺

# CP1251 → KOI8-R
# CP1251 → CP866
# CP855 → MACCYRILLIC


KEYWORD = "Левин"
CODINGS = ["KOI8-R", "CP1251", "CP866", "MACCYRILLIC", "ISO-8859-5", "CP855"]
ALPH = """!"'(),-.0123456789:;?ABCDEFHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя \t\n"""


# tmp
def _input_example():
    s = """     - Она не то  что  скучает,  но  эта  неопределенность,  нерешительность
    положения, - слышал Левин  и  хотел  поспешно  отойти;  но  Степан  Аркадьич
    подозвал его.
        - Левин! - сказал Степан Аркадьич, и  Левин  заметил,  что  у  него  на"""

    bytes = s.encode("KOI8-R")
    bytes = bytes.decode("CP1251").encode("KOI8-R")
    bytes = bytes.decode("CP1251").encode("CP866")
    bytes = bytes.decode("CP855").encode("MACCYRILLIC")

    return bytes


# input_bytes = _input_example()
input_bytes = sys.stdin.buffer.read()


target_map = {}
codings_map = {}
target_map[ALPH.encode("KOI8-R")] = KEYWORD.encode("KOI8-R")
codings_map[ALPH.encode("KOI8-R")] = ["KOI8-R"]


# Генератор комбинаций кодировок (без одинаковых соседних элементов)
def coding_indices_generator():
    indices = lambda: range(len(CODINGS))
    for i in indices():
        for j in indices():
            if i == j:
                continue
            yield (i, j)


arr = [ALPH.encode("KOI8-R")]
decode_and_encode = lambda word, i, j: word.decode(CODINGS[i]).encode(CODINGS[j])

while arr:
    word = arr.pop()
    for i, j in coding_indices_generator():
        try:
            new_word = decode_and_encode(word, i, j)
            if new_word in codings_map.keys():
                continue

            codings_map[new_word] = codings_map[word] + [CODINGS[i]] + [CODINGS[j]]
            target_map[new_word] = decode_and_encode(target_map[word], i, j)
            arr.append(new_word)
        except:
            pass


for key, value in target_map.items():
    if not value in input_bytes:
        continue

    counter = 0
    for step in reversed(codings_map[key]):
        if (counter % 2) == 0:
            input_bytes = input_bytes.decode(step)
        else:
            input_bytes = input_bytes.encode(step)
        counter += 1

    break

print(input_bytes)
