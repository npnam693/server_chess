from flask import Flask
import socket_setup

app = Flask(__name__)

@app.route('/')
def run_server():
    return 'Server is running'

if __name__ == '__main__':
    socket_setup.socket_run()   
    app.run(debug=True)