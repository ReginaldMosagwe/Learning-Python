from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = ["Believe in yourself.",
    "Stay hungry, stay foolish.",
    "Every day is a second chance.",
    "Don't watch the clock; do what it does. Keep going.",
    "Be the change you wish to see in the world."]

@app.route('/')
def index():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)