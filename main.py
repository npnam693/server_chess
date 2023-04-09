from flask import Flask
import socket_setup

app = Flask(__name__)

@app.route('/')
def run_server():
    socket_setup.socket_run()   
    return 'Server is running'

if __name__ == '__main__':
    app.run()