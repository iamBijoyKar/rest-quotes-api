from flask import Flask,jsonify

import random

quotes = [
  "If you want to be happy, be. - Leo Tolstoy",
  "It is not enough to be busy. So are the ants. The question is: What are we busy about? - Henry David Thoreau",
  "The only way to do great work is to love what you do. - Steve Jobs"
]

app = Flask(__name__)

@app.route('/api/quotes/random')
def generate_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == '__main__':
  app.run()
