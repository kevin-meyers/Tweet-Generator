from flask import Flask, render_template, request

from markov_chain import MarkovChain

from random import shuffle

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/returned', methods=['POST'])
def r():
    mv = MarkovChain(int(request.form.get('n')))
    mv.build_markov('data/sherlock_holmes.txt')


    return ' '.join(mv.generate_sentence())
