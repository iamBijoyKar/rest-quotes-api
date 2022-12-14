from flask import Flask,jsonify
from quote import quoteGenerate


app = Flask(__name__)

@app.route('/api/quotes/random')
def generate_random_quote():
    quote = quoteGenerate()
    return jsonify(quote)

if __name__ == '__main__':
  app.run()
