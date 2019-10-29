import sys
import random


def get_words(num_words):
    # 102305 is the number of words in the dict.
    lines = [int(random.random() * 102305) for _ in range(num_words)]
    with open('/usr/share/dict/american-english', 'r') as f:
        return [line.strip() for index, line in enumerate(f) if index in lines]


if __name__ == '__main__':
    num_words = int(sys.argv[1])
    selected = get_words(num_words)

    print(' '.join(selected))
