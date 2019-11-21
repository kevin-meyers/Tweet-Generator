import sys

def reverse_word(word):
    return word[::-1]


if __name__ == '__main__':
    inputs = sys.argv[1:]
    print(reverse_word(' '.join(inputs)))
