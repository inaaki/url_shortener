from flask import Flask, render_template, request, redirect
from src.db import add_to_db, check_url

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
    urls = check_url(short_url)
    if urls:
        return redirect(urls[1])
    return "Not Found"
