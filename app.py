from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Do not watch the clock. Do what it does. Keep going.",
    "Everything you’ve ever wanted is on the other side of fear.",
    "Success is not the key to happiness. Happiness is the key to success."
]

@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)
