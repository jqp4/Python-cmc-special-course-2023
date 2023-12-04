# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_SemClass


DEBUG_MODE = False


def pprint(*args, **kwargs):
    if DEBUG_MODE:
        print(end="         ")
        print(*args, **kwargs)


class SemaphoreDescriptor:
    _captured_semaphores = set()

    # Внутрянняя функция освобождения семафора
    def _release_semaphore(self, semaphore_name):
        if semaphore_name in self._captured_semaphores:
            self._captured_semaphores.remove(semaphore_name)

    # Захват семафора
    def __get__(self, obj, _):
        pprint(f"Try to get {repr(obj)}.lock:")

        if not obj._semaphore_name in self._captured_semaphores:
            self._captured_semaphores.add(obj._semaphore_name)
            obj._semaphore_owner = True

        if obj._semaphore_owner:
            return obj._semaphore_name

        return None

    # Регистрация семафора + освобождение предыдущего
    def __set__(self, obj, new_semaphore_name):
        pprint(f"Set {repr(obj)}.lock = {new_semaphore_name}")

        if obj._semaphore_owner:
            self._release_semaphore(obj._semaphore_name)
            obj._semaphore_owner = False

        obj._semaphore_name = new_semaphore_name

    # Освобождение семафора, если он захвачен именно этим lock-ом
    def __delete__(self, obj):
        pprint(f"Delete {repr(obj)}.lock")

        if obj._semaphore_owner:
            self._release_semaphore(obj._semaphore_name)
            obj._semaphore_owner = False

        obj._semaphore_name = False


class Lock:
    def locked(cls):
        class Locked(cls):
            lock = SemaphoreDescriptor()

            def __init__(self, *args, **kwargs):
                self._semaphore_name = None
                self._semaphore_owner = False
                super(cls, Locked).__init__(*args, **kwargs)

            def __del__(self):
                pprint(f"Delete {repr(self)} obj:")

                del self.lock

                if "__del__" in super(cls).__dir__():
                    pprint(f"Delete {repr(self)} obj")
                    super(cls).__del__()

        return Locked
