#app.py


'''Dependências'''
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
import time
import logging


app = Flask(__name__) #Criação de instância 
socketio = SocketIO(app) # Instanciamos o SocketIO com o nosso aplicativo Flask para adicionar suporte à comunicação em tempo real.

#Definimos duas URLS pro aplicativo (btc e eth)
@app.route('/bitcoin')
def bitcoin():
    return render_template('btc.html') #Mostra o arquivo btc.html quando alguém acessa a URL /bitcoin.

@app.route('/ethereum')
def ethereum():
    return render_template('eth.html') 

def fetch_data(): #Função fica buscando preços do Bitcoin e Ethereum a cada 5 segundos.
    while True:
        try:
            
            btc_response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json') #Faz uma requisição à API para buscar os dados
            btc_response.raise_for_status() #Verifica se a requisição foi bem-sucedida
            btc_data = btc_response.json() #Converte a resposta da API de Bitcoin para formato JSON
            
            eth_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
            eth_data = eth_response.json()

            #Envia (emite) os preços atualizados para todos os navegadores conectados em tempo real.
            socketio.emit('updateBitcoin', {'btc_price': btc_data['bpi']['USD']['rate']}) 
            socketio.emit('updateEthereum', {'eth_price': eth_data['ethereum']['usd']})
        
        # Captura e loga qualquer erro que possa acontecer ao tentar buscar os dados da API.
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao buscar dados: {e}")

        time.sleep(5)

@socketio.on('connect')
def handle_connect(): #Especifica que a função handle_connect() deve ser executada sempre que um novo usuário se conectar ao aplicativo.
    socketio.start_background_task(target=fetch_data)
    '''socketio.start_background_task(target=fetch_data): Inicia a função fetch_data() em segundo plano 
    quando um usuário se conecta, para que o servidor continue funcionando enquanto os dados são buscados.'''

if __name__ == '__main__':
    socketio.run(app)
