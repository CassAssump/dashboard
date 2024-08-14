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
        # Exemplo de busca de dados de Bitcoin e Ethereum
        btc_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        eth_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')

        btc_data = btc_response.json()
        eth_data = eth_response.json()

        socketio.emit('updateData', {
            'btc_price': btc_data['bpi']['USD']['rate'],
            'eth_price': eth_data['ethereum']['usd']
        })
        time.sleep(5)  # Espera 5 segundos antes de buscar novos dados

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(target=fetch_data)

if __name__ == '__main__':
    socketio.run(app)
