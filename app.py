import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    with open('usaLow.svg') as f:
        return render_template('index.html', map_text=f.read())

if __name__ == '__main__':
    app.run()