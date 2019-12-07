from data_struct_algo.queues.circular_buffer import CircularBuffer

START_TOKEN = '#START'
END_TOKEN = '#END'


class MarkovChain(dict):
    '''MarkovChain is a dictionary implementation of a markov chain.'''

    def __init__(self, n=1):
        self.n = n

    def __missing__(self, key):
        self[key] = Dictogram()

        return self[key]

    @staticmethod
    def get_words_list(path_to_file):
        f = open(path_to_file, 'r')
        for line in f:
            yield START_TOKEN
            for word in line.split():
                yield word.strip()

            yield END_TOKEN

    def build_markov(self, path_to_file):
        previous_n = CircularBuffer(fixed_size=self.n)
        words = self.get_words_list(path_to_file)

        for word in words:
            if word is START_TOKEN:
                previous_n.empty()
                for _ in range(self.n):
                    previous_n.enqueue(next(words))

                self[START_TOKEN].add_count(previous_n)
                print(previous_n)
                continue

            self[previous_n].add_count(word)
            previous_n.enqueue(word)

    def generate_sentence(self):
        previous_n = self[START_TOKEN].sample()

        count = 0
        while count <= 20:
            word = self[previous_n].sample()
            if word is END_TOKEN:
                break

            count += 1
            previous_n.enqueue(word)
            yield word


if __name__ == '__main__':
    from dictogram import Dictogram
    mv = MarkovChain(2)
    mv.build_markov('data/test.txt')
    #for word in mv.get_words_list('data/test.txt'):
     #   print(word)
    print(mv[START_TOKEN])
    #print(list(mv.generate_sentence()))

else:
    from .dictogram import Dictogram
