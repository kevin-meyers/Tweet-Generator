import sys

from random import shuffle


def make_anagram(solved):
    shuffle(solved)
    return solved

if __name__ == '__main__':
    inputs = sys.argv[1:]
    if len(inputs) > 1:
        print(' '.join(make_anagram(inputs)))

    else:
        print(''.join(make_anagram(list(inputs[0]))))
