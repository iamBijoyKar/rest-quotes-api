from flask import Flask,jsonify,render_template,url_for
import json
import random

def quoteGenerate():
  with open('quotes.json','r') as f:
    data = json.load(f)
    quote = random.choice(data)
    print(quote)
    return quote

app = Flask(__name__)

@app.route('/')
def redirect():
  return render_template('redirect.html')

@app.route('/api')
def home():
  return render_template('index.html')

@app.route('/api/quotes/random')
def generate_random_quote():
  quote = quoteGenerate()
  return jsonify(quote)

@app.route('/api/quotes')
def generate_quotes():
  with open('quotes.json','r') as f:
    quotes = json.load(f)
    # print(quotes)
  return jsonify({'quotes':quotes})

if __name__ == '__main__':
  app.run()
