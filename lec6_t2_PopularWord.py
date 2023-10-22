# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_PopularWord

words_map = {}
line = input()

while line:
    for word in line.split():
        words_map[word] = words_map.get(word, 0) + 1
        
    line = input()

max_num = max(words_map.values())
most_common_words = [word for word, num in words_map.items() if num == max_num]

if len(most_common_words) == 1:
    print(most_common_words[0])
else:
    print("---")
