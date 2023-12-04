# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_DefArgs


from inspect import signature, _empty as empty_type


def DefArgs(*default_args):
    def decorator(func):
        # Получение данных о параметрах декорируемой функции
        func_params = signature(func).parameters
        func_params_num = len(func_params.values())

        # Если дефолтных параметров указано меньше чем у декорируемой функции, выдаем ошибку
        if len(default_args) < func_params_num:
            raise TypeError

        def new_func(*args):
            # Если у новой функции получили больше параметров чем было в изначальной, выдаем ошибку
            if len(args) > func_params_num:
                raise TypeError

            # Функция составления одного нового аргумента по индексу (merge)
            def complete_arg(index):
                default_arg = default_args[index]
                arg = args[index] if len(args) > index else None

                if arg == None:
                    return default_arg
                elif isinstance(arg, type(default_arg)) or isinstance(arg, empty_type):
                    return arg
                else:
                    raise TypeError

            # Составляем список новых аргументов и вызываем изначальную функцию
            complete_args = [complete_arg(i) for i in range(func_params_num)]
            return func(*complete_args)

        return new_func

    return decorator


# @DefArgs(2, 3, 4)
# def mult(a, b):
#     return a * b


# for args in (), (4,), (7, 8), (7, 8, 9), ("q", "w"):
#     # print(f"params: {args}:", end=" ")
#     try:
#         print(mult(*args))
#     except TypeError:
#         print("Nope")

# try:
#     @DefArgs(2)
#     def mult(a, b):
#         return a * b
# except TypeError:
#     print("Nope")

# 6
# 12
# 56
# Nope
# Nope
# Nope
