# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_TriangleSquare

from decimal import Decimal, getcontext


coordinates = input().replace(" ", "").split(",")

max_coords_len = 0

for coordinate in coordinates:
    if max_coords_len < len(coordinate):
        max_coords_len = len(coordinate)

x1 = Decimal(coordinates[0])
y1 = Decimal(coordinates[1])
x2 = Decimal(coordinates[2])
y2 = Decimal(coordinates[3])
x3 = Decimal(coordinates[4])
y3 = Decimal(coordinates[5])

getcontext().prec = max_coords_len * 4
area = abs(Decimal("0.5") * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

normalized = area.normalize()
exp = normalized.as_tuple()[2]
answer = normalized if exp <= 0 else normalized.quantize(1)

print(answer)
