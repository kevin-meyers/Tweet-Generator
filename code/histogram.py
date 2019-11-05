from collections import defaultdict



class Histogram:
    def __init__(self):
        self.unique_words = 0
        self.num_words = 0
        self.hist = defaultdict(lambda: self._increment_unique())

    def __len__(self):
        return self.unique_words

    def _increment_unique(self):
        self.unique_words += 1
        return 0

    @staticmethod
    def _open_file(filepath):
        f = open(filepath, 'r')
        for line in f:
            for word in line.split():
                yield word

    def build_histogram(self, filepath):
        for word in self._open_file(filepath):
            self.num_words += 1
            self.hist[word] += 1

    def get_frequency(self, word):
        return self.hist[word]

    def get_proba_offset(self):
        running_sum = 0.0
        for word, freq in self.hist.items():
            running_sum += freq / self.num_words
            yield word, running_sum
