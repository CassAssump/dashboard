from flask import Flask, render_template, redirect, url_for
from flask_socketio import SocketIO, emit
import requests
import time
import logging

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return redirect(url_for('bitcoin'))

@app.route('/bitcoin')
def bitcoin():
    return render_template('btc.html')

@app.route('/ethereum')
def ethereum():
    return render_template('eth.html')

def fetch_data():
    while True:
        try:
            btc_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
            btc_response.raise_for_status()
            btc_data = btc_response.json()
            
            eth_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
            eth_data = eth_response.json()

            socketio.emit('updateBitcoin', {'btc_price': btc_data['bpi']['USD']['rate']})
            socketio.emit('updateEthereum', {'eth_price': eth_data['ethereum']['usd']})
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao buscar dados: {e}")

        time.sleep(5)

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(target=fetch_data)

if __name__ == '__main__':
    socketio.run(app)
