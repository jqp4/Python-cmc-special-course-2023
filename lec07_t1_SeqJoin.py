# task: https://uneex.org/LecturesCMC/PythonIntro2023/Homework_SeqJoin


def joinseq(*args):
    iterators = []
    first_elements = []

    for arg in args:
        iterator = iter(arg)
        iterators.append(iterator)
        first_elements.append(next(iterator, None))

    while True:
        min_index = None
        min_element = None

        for index, element in enumerate(first_elements):
            if element != None:
                if min_element == None or element < min_element:
                    min_element = element
                    min_index = index

        if min_element == None:
            break

        yield min_element
        first_elements[min_index] = next(iterators[min_index], None)
