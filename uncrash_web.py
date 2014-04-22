from flask import Flask, render_template, request
import uncrash, random, urllib.parse

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/solve", methods = ['POST', 'GET'])
def solve():
    if request.method == 'POST':
        starter = request.form['starter'].upper()
        word_size = len(starter)
        thesaurus = uncrash.load_words(word_size)
        words = uncrash.uncrash(thesaurus, [starter])
    else:
        words = []
    return render_template('solve.html', uncrash = words)

if __name__ == "__main__":
    app.debug = True
    app.run()
