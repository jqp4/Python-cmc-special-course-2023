# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_ObjInfo


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Create an instance once
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class ObjectInfo(metaclass=Singleton):
    def __init__(self):
        self.created_objects_num = 0
        self.living_objects_num = 0
        self.all_tilde_operations_num = 0

    def add_object(self):
        self.created_objects_num += 1
        self.living_objects_num += 1

    def remove_object(self):
        self.living_objects_num -= 1


class Shared:
    def __init__(self):
        self.objectInfo = ObjectInfo()
        self.objectInfo.add_object()
        self.local_tilde_operations_num = 0

    def __del__(self):
        self.objectInfo.remove_object()

    def __str__(self):
        return f"|{self.objectInfo.created_objects_num}/{self.objectInfo.living_objects_num}/{self.objectInfo.all_tilde_operations_num}/{self.local_tilde_operations_num}|"

    def __invert__(self):
        self.objectInfo.all_tilde_operations_num += 1
        self.local_tilde_operations_num += 1
        return self.local_tilde_operations_num


# # test
# b, c = Shared(), Shared()
# print(b, c, Shared())
# print(~c, ~b, ~c)
# print(b, c)
