from flask import Flask, render_template, request
from src.db import add_to_db

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        short = add_to_db(url)
        if short:
            short = request.host_url + short
        return render_template('index.html', short=short, long=url)
    else:
        return render_template('index.html')


@app.route('/<short_url>')
def redirect_to_url(short_url):
    # check if url exists to db
    #     if exists:
    #         redirect to that url
    #     else:
    #         redirect to not found
    pass
