# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_FindRect

# Морской бой

# Ввести несколько строк одинаковой длины, состоящих из символов «#» и «.».
# Ввод заканчивается пустой строкой. На получившемся поле изображены только
# прямоугольники, причём они не соприкасаются даже углами. Вывести количество
# этих прямоугольников.

# 1. Возможно, удобнее всего хранить это в виде списка строк.
# 2. Никакие из условий/свойств ввода проверять, как обычно, не надо


counter = 0
newLineStr = input()
lineWidth = len(newLineStr)
prevLine = [0 for _ in range(lineWidth)]

while newLineStr:
    thisLine = [0 for _ in range(lineWidth)]
    for i in range(0, lineWidth):
        if newLineStr[i] == "#":
            if prevLine[i] != 0:
                thisLine[i] = prevLine[i]
            elif i >= 1 and thisLine[i - 1] != 0:
                thisLine[i] = thisLine[i - 1]
            else:
                counter += 1
                thisLine[i] = counter

    prevLine = thisLine
    newLineStr = input()

print(counter)
