from data_struct_algo.queues.circular_buffer import CircularBuffer

from dictogram import Dictogram

START_TOKEN = '#START'
END_TOKEN = '#END'


class MarkovChain(dict):
    '''MarkovChain is a dictionary implementation of a markov chain.'''

    def __init__(self, n=1):
        self.n = n

    def __missing__(self, key):
        ''' If the key isnt in the markovchain, add it and give it a Dictogram. '''
        self[key] = Dictogram()

        return self[key]

    @staticmethod
    def add_tokens(line):
        ''' Makes a generator of the words in a sentence and adds END_TOKEN. '''
        for word in line.split():
            yield word.strip()

        yield END_TOKEN

    def get_sentences(self, path_to_file):
        ''' Opens the file and reads it line by line, returning line
        generators.

        '''
        f = open(path_to_file, 'r')
        for line in f:
            yield self.add_tokens(line)

    def add_sentence(self, sentence):
        ''' Uses a CircularBuffer to hold the previous self.n words,
        adds the current word to the transitions Dictogram.

        '''
        previous_n = CircularBuffer(fixed_size=self.n, initial_value=START_TOKEN)
        for word in sentence:
            buffer_words = str(previous_n)
            self[buffer_words].add_count(word)
            previous_n.enqueue(word)

    def build_markov(self, path_to_file):
        ''' Adds sentences one by one to self. '''
        for sentence in self.get_sentences(path_to_file):
            self.add_sentence(sentence)

    def generate_sentence(self):
        ''' Infers a possible sentence. '''
        previous_n = CircularBuffer(fixed_size=self.n, initial_value=START_TOKEN)
        count = 0
        word = None
        while count <= 20:
            buffer_words = str(previous_n)
            word = self[buffer_words].sample()
            previous_n.enqueue(word)
            if word is END_TOKEN:
                break

            yield word
            count += 1


if __name__ == '__main__':
    mv = MarkovChain(2)
    mv.build_markov('data/sherlock_holmes.txt')
    #for word in mv.get_words_list('data/test.txt'):
     #   print(word)
    print(list(mv.generate_sentence()))
