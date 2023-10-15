# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_PatternFind

mark = "@"


# выдает индексы всех совпадений в строке
def find_all_occurrences(a, sub):
    start = 0
    while True:
        start = a.find(sub, start)
        if start == -1:
            return

        yield start
        start += len(sub)


# выдает индексы для проверки
def find_all(a, sub):
    shift = 0
    while sub[shift] == mark:
        shift += 1

    for index in find_all_occurrences(a, sub[shift:]):
        if index - shift < 0:
            continue

        yield index - shift


def get_first_word(b):
    shift = 0
    while b[shift] == mark:
        shift += 1

    first_mark = b.find(mark, shift)
    if first_mark == -1:
        return b

    return b[: b.find(mark, shift)]


def check_b_consists_of_marks(b):
    for char in b:
        if char != mark:
            return False

    return True


def lec5_task1(a, b):
    if check_b_consists_of_marks(b):
        return 0 if len(b) <= len(a) else -1

    first_word = get_first_word(b)
    for i0 in find_all(a, first_word):
        flag = True
        for i in range(len(first_word), len(b)):
            if b[i] != mark and a[i0 + i] != b[i]:
                flag = False
                break
        if flag:
            return i0
    return -1


print(lec5_task1(input(), input()))


# tests = [
#     ("lorem ipsum, quia dolor sit, amet, consectetur", "dolor @it,@@met", 18),
#     ("qweqwe wertsaq ertsqa wertgad wertgard", "wer@ga", 22),
#     ("qwerqwer qwer qwe rqwe rqwerqwe rqwer", "rque", -1),
#     ("qwerwq er bababaobaber", "ba@ba", 14),
#     ("Hello Darkness my old friend, I come to talk with u again", "@@ain", 52),
#     ("sadfqwef qwef qwef", "@", 0),
# ]


# for a, b, true_ans in tests:
#     print(f"{a}\n{b}")

#     ans = lec5_task1(a, b)
#     print(f"ans: {ans}")

#     if ans == true_ans:
#         print("YES\n")
#     else:
#         print("NO\n")
