
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f'<b>Hello from {escape(name)}!</b>'

