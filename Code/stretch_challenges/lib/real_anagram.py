from collections import defaultdict
import sys

class AnagramHolder:
    def __init__(self):
        self.anagram_dict = defaultdict(lambda: [])

    @staticmethod
    def open_file(filepath):
        f = open(filepath, 'r')
        for word in f:
            yield word.strip()


    def fill_dict(self, filepath):  # Consider writing my own sorting.
        for ind, word in enumerate(self.open_file(filepath)):
            self.anagram_dict[str(sorted(word))].append(word)

    def find_anagrams(self, word):
        return self.anagram_dict[str(sorted(word))]


if __name__ == '__main__':
    ah = AnagramHolder()
    ah.fill_dict('/usr/share/dict/american-english')

    while True:
        user_in = input('Enter a word you want anagramed. Type / to quit: ')
        if user_in == '/':
            break

        print(ah.find_anagrams(user_in))
