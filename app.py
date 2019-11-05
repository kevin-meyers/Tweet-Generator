from flask import Flask, render_template, request

from code.histogram import Histogram
from code.sample import WordFreqTree


app = Flask(__name__)

hist = Histogram()
tree = WordFreqTree()

hist.build_histogram('code/data/sherlock_holmes.txt')
words_freq = hist.get_proba_offset()

tree.build_tree(words_freq)


@app.route('/')
def home():
    print('works?')
    return render_template('index.html')


@app.route('/more-words', methods=['POST'])
def more_words():
    num_words = int(request.form.get('num-words'))
    return ' '.join([tree.sample() for _ in range(num_words)])
