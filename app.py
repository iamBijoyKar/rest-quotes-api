from flask import Flask,jsonify
import json
import random

def quoteGenerate():
  with open('quotes.json','r') as f:
    data = json.load(f)
    quote = random.choice(data)
    print(quote)
    return quote

app = Flask(__name__)

@app.route('/api/quotes/random')
def generate_random_quote():
  quote = quoteGenerate()
  return jsonify(quote)

if __name__ == '__main__':
  app.run()
