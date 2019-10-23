import sys

from random import sample

with open('/usr/share/dict/american-english', 'r') as f:
    words = [line.strip() for line in f.readlines()]

def get_words(num_words):
    return sample(words, num_words)


if __name__ == '__main__':
    num_words = int(sys.argv[1])
    selected = get_words(num_words)

    print(' '.join(selected))
