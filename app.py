from flask import Flask
from socket_setup import socket_run

app = Flask(__name__)
@app.route('/')
def run_server():
    socket_run()
    return 'Server is running'

if __name__ == '__main__':
    app.run()
