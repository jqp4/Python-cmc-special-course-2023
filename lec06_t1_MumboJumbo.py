# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_MumboJumbo

consonants = "bcdfgjklmnpq stvxzhrw"
letters_sets = [set(), set()]
word = input()
num = 0

while word:
    for letter in word:
        if letter in consonants:
            if not letter in letters_sets[num]:
                letters_sets[num].add(letter)

    word = input()
    num = 1 if num == 0 else 0


if len(letters_sets[0]) > len(letters_sets[1]):
    print("Mumbo")
else:
    print("Jumbo")
