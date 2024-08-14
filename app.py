# app.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
import time

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def fetch_data():
    while True:
        # Exemplo de busca de dados de uma API externa
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        data = response.json()
        socketio.emit('updateData', {'price': data['bpi']['USD']['rate']})
        time.sleep(5)  # Espera 5 segundos antes de buscar novos dados

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(target=fetch_data)

if __name__ == '__main__':
    socketio.run(app)
