# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_SafeEval


def safeval(__source, __globals=None, __locals=None):
    globals_copy = globals().copy()
    try:
        return eval(__source, __globals, __locals)
    except NameError:
        return __source
    except Exception as e:
        return e
    finally:
        for key, value in globals_copy.items():
            if not key in globals():
                globals()[key] = value

        globals_finally = globals().copy()
        for key, value in globals_finally.items():
            if not key in globals_copy:
                del globals()[key]
