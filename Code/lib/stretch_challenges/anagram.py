import sys

from .utils.my_random import shuffle


def make_anagram(inputs):
    solved = prepare_input(inputs)
    shuffle(solved)
    return ''.join(solved)

def prepare_input(inputs):
    if len(inputs) > 1:
        return [i + ' ' for i in inputs]

    else:
        return list(inputs[0])

if __name__ == '__main__':
    inputs = sys.argv[1:]
    print(make_anagram(inputs))
