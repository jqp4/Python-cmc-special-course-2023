# ejudge: https://ejudge.cs.msu.ru/client?SID=0b72bb6a838388b3&action=139&prob_id=13
# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_AllProducts


# Ввести произвольное натуральное число, не превосходящее 1000000000, и вывести (через «*») 
# все его разложения на натуральные сомножители, превосходящие 1, без учёта перестановок. 
# Сомножители в каждом разложении и сами разложения (как последовательности) при выводе 
# должны быть упорядочены по возрастанию. Само число также считается разложением. 
# Можно использовать рекурсию.


def AllProducts(x, divs):
    if x == 1:
        for div in divs[:-1]:
            print(div, end="*")
        print(divs[-1])
        return

    max_div = int(x**0.5) + 1
    for i in list(range(2, max_div)) + [x]:
        if x % i == 0 and (not divs or i >= divs[-1]):
            divs.append(i)
            AllProducts(x // i, divs)
            divs.pop()


AllProducts(eval(input()), [])
