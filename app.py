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
        try:
            btc_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
            btc_response.raise_for_status()  # Verifica se houve algum erro na requisição
            btc_data = btc_response.json()

            socketio.emit('updateData', {
                'price': btc_data['bpi']['USD']['rate'],  # Campo ajustado para 'price'
            })
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados: {e}")

        time.sleep(5)  # Espera 5 segundos antes de buscar novos dados

@socketio.on('connect')
def handle_connect():
    socketio.start_background_task(target=fetch_data)

if __name__ == '__main__':
    socketio.run(app)
