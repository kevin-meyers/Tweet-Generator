from flask import Flask, render_template, request

from Code.lib.default_challenges.markov_chain import MarkovChain

from random import shuffle

app = Flask(__name__)


mv = MarkovChain()
mv.build_markov('Code/lib/default_challenges/data/test.txt')


#@app.route('/')
#def home():
#    return render_template('index.html')


@app.route('/')
def markov_sentence():
    return str(list(mv.generate_sentence()))
