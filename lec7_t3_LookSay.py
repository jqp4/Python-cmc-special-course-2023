# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_LookSay

# Algo: https://oeis.org/A034002
# Wiki: https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%C2%AB%D0%9F%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B8-%D0%B8-%D1%81%D0%BA%D0%B0%D0%B6%D0%B8%C2%BB


def LookSay():
    current_values = "1"
    next_values = ""
    s = 1

    while True:
        x = current_values + " "

        for i in current_values:
            yield int(i)

        for i in range(len(x) - 1):
            if x[i] == x[i + 1]:
                s += 1
            else:
                next_values += str(s) + str(x[i])
                s = 1

        current_values = next_values
        next_values = ""
        s = 1
