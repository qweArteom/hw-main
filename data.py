from flask import Flask, render_template
from data import title, subtitle, description, departures, tours

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title=title, subtitle=subtitle, description=description, departures=departures)

@app.route('/tours')
def tours_page():
    return render_template('tours.html', title=title, tours=tours)

if __name__ == '__main__':
    app.run(debug=True)