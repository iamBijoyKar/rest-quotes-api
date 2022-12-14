import json
import random

def quoteGenerate():
    with open('quotes.json','r') as f:
        data = json.load(f)
        quote = random.choice(data)
        print(quote)
        return quote

