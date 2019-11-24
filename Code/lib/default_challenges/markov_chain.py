from dictogram import Dictogram


START_TOKEN = '#START'
END_TOKEN = '#END'


class MarkovChain(dict):
    '''MarkovChain is a dictionary implementation of a markov chain.'''

    def __init__(self):
        super(MarkovChain, self).__init__()  # Initialize as a dict

    def __missing__(self, key):
        self[key] = Dictogram()

        return self[key]


    @staticmethod
    def get_words_list(path_to_file):
        f = open(path_to_file, 'r')
        for line in f:
            for word in line.split():
                yield word.strip()

            yield END_TOKEN

    def build_markov(self, path_to_file):
        previous = START_TOKEN
        for word in self.get_words_list(path_to_file):
            self[previous].add_count(word)

            previous = word

    def generate_sentence(self):
        word = START_TOKEN
        count = 0
        while word != END_TOKEN and count <= 20:
            word = self[word].sample()
            count += 1
            yield word


if __name__ == '__main__':
    mv = MarkovChain()
    mv.build_markov('data/test.txt')
    print(list(mv.generate_sentence()))
