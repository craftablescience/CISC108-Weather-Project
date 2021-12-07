from flask import Flask
app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello, World!'


@app.route('/lmao/')
def lmao():
    return "lol troled xd"
