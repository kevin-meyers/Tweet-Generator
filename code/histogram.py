from collections import defaultdict


class Histogram:
    def __init__(self, filepath):
        self.filepath = filepath
        self.unique_words = 0
        self.hist = defaultdict(lambda: _incrememnt_unique())

    def _incrememnt_unique():
        self.unique_words += 1
        return 0

    def _open_file(self):
        f = open(self.filepath, 'r')
        for line in f:
            for word in line:
                yield word

    def build_histogram(self):
        for word in self._open_file():
            self.hist[word] += 1

    def get_frequency(word):
        return self.hist[word]



'''
    def hist_list(filepath):
        hist = []
        index = 0
        ids = {}
        for word in enumerate(open_file):
            if word not in ids:
                ids[index] = word

            if len(hist) >= index:
                hist[index] += 1

            else:
                hist.append(0)

        return hist, ids
'''
