# task: http://uneex.org/LecturesCMC/PythonIntro2023/Homework_MultTable

# https://note.nkmk.me/en/python-format-zero-hex/
# https://stackoverflow.com/questions/36962995/format-in-python-by-variable-length


N, M = eval(input())

N_len = len(str(N))
NxN_len = len(str(N * N))
line_separator = "=" * M
columns_separator = ".|."
max_column_len = len(f"{N}.*.{N}.=.{N*N}")
formatting_s = "{0:.>{3}}.*.{1:.<{4}}.=.{2:.<{5}}"


def get_max_str_len(max_columns_num):
    return max_column_len * max_columns_num + len(columns_separator) * (
        max_columns_num - 1
    )


max_columns_num = 1
while get_max_str_len(max_columns_num + 1) <= M:
    max_columns_num += 1

print(line_separator)

start_int = 1
while start_int <= N:
    columns_num = min(max_columns_num, N - start_int + 1)

    for i in range(1, N + 1):
        for column_num in range(columns_num):
            j = start_int + column_num
            sep = "\n" if column_num + 1 == columns_num else columns_separator

            print(
                formatting_s.format(j, i, i * j, N_len, N_len, NxN_len),
                end=sep,
            )

    print(line_separator)
    start_int += max_columns_num
