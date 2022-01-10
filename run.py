from flask import Flask
import socket


app = Flask(__name__)


@app.route('/')
def index():
    return f'Index {socket.gethostname()}'


if __name__ == '__main__':
    app.run()
