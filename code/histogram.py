from collections import defaultdict

def open_file(filepath):
    f = open(filepath, 'r')
    for line in f:
        for word in line:
            yield word


def histogram(filepath):
    hist = defaultdict(lambda: 0)
    for word in open_file(filepath):
        hist[word] += 1

    return hist

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


def unique_words(hist):
    return len(hist)

def frequency(word, hist):
    return hist[word]


