# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_IterPi

# Wiki: https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%A7%D1%83%D0%B4%D0%BD%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BEs

from decimal import Decimal as dec
import decimal


# Factorial for Chudnovsky PI formula
def fpi(k, n):
    x = k * n
    result = 1

    for i in range(1, n + 1):
        result *= x + i

    return result


def PiGen():
    dec1 = dec("1")
    dec2 = dec("13591409")
    dec3_const = dec(640320) ** 3
    dec4_const = dec("10005").sqrt() * 426880

    pi = dec1 * dec2
    k = 0

    while True:
        dec1 *= -dec(fpi(k, 6) / (fpi(k, 3) * fpi(k, 1) ** 3 * dec3_const))
        dec2 += 545140134
        pi += dec1 * dec2

        pi_str = str(1 / pi * dec4_const)
        yield pi_str[k]
        k += 1


decimal.getcontext().prec = 2000
