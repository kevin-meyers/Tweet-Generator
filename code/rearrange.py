import sys

from my_random import shuffle

def rearrange(words_list):
    shuffle(words_list)
    return ' '.join(words_list)


if __name__ == '__main__':
    words_list = sys.argv[1:]
    print(rearrange(words_list))
