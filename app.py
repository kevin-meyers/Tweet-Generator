from flask import Flask, render_template, request

from code.histogram import Histogram
from code.word_freq_tree import WordFreqTree

from random import shuffle

app = Flask(__name__)

hist = Histogram()
tree = WordFreqTree()

hist.build_histogram('code/data/sherlock_holmes.txt')
words_freq = list(hist.get_proba_offset())
shuffle(words_freq)

tree.build_tree(words_freq)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/more-words', methods=['POST'])
def more_words():
    num_words = int(request.form.get('num-words'))
    return ' '.join([tree.sample() for _ in range(num_words)])
