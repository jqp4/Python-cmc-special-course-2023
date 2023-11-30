# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_ZipInfo

from sys import stdin
from zipfile import ZipFile
from io import BytesIO

# user_input = ""
# for line in stdin:
#     if line == "\n":
#         break
#     user_input += line
# raw_data = bytes.fromhex(user_input)

raw_data = bytes.fromhex(stdin.read())
zip_file = ZipFile(BytesIO(raw_data), "r")

count = 0
zip_size = 0

for element in zip_file.infolist():
    if not element.is_dir():
        count += 1
        zip_size += element.file_size

print(count, zip_size)
