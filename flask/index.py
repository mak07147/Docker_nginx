from flask import Flask
import datetime
import socket

app = Flask(__name__)


@app.route('/servername')
def hello_world():
    return f"Hostname: {socket.gethostname()} <br> IP Address: {socket.gethostbyname(socket.gethostname())}"

@app.route('/')
def index():
    return 'Главная страница <br> Дата и время: {}'.format(str(datetime.datetime.now())) 

@app.route('/greetings')
def greetings():
    return 'Greetings'

if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)