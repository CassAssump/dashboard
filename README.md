<h1>📚 Real-Time Bitcoin Price Dashboard</h1>

<p>Este projeto é uma aplicação web em tempo real que exibe o preço atual do Bitcoin em USD. Ele utiliza Flask para o backend e Flask-SocketIO para comunicação em tempo real entre o servidor e o frontend.</p>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li><strong>Rota de Boas-Vindas</strong>: Uma rota simples que retorna uma mensagem de boas-vindas.</li>
  <li><strong>Rota para Obter Dados de Restaurantes</strong>: Faz uma requisição para uma API externa que retorna dados de restaurantes e permite filtrar por nome de restaurante.</li>
</ul>

<h2>🛠 Tecnologias Utilizadas</h2>
<ul>
  <li><strong>Python 3.7+</strong></li>
  <li><strong>Flask</strong> (Framework web em Python para criar o backend.)</li>
  <li><strong>Flask-SocketIO (Biblioteca para comunicação em tempo real via WebSockets.)</li>
  <li><strong>HTML and CSS</strong> (Para a estrutura e o estilo da interface do usuário.)</li>
  <li><strong>Requests</strong> (Biblioteca para fazer requisições HTTP)</li>
</ul>

<h2>📦 Estrutura do Projeto</h2>
<pre>
pagina/
├── app.py                # Código do backend em Python
├── templates/            # Diretório para arquivos HTML
│   └── index.html        # Código do frontend
└── static/               # Diretório para CSS, JS, e outros arquivos estáticos
    └── style.css         # Arquivo de estilo CSS

</pre>

<h2>🚧 Como Executar o Projeto</h2>

<h3>Pré-requisitos</h3>
<ul>
  <li>Certifique-se de ter o Python 3.7 ou superior instalado.</li>
  <li>É recomendável usar um ambiente virtual para evitar conflitos de dependências.</li>
</ul>

<h3>Passo a Passo</h3>
<ol>
  <li><strong>Clone este repositório:</strong>
    <pre><code>git clone https://github.com/CassAssump/dashboard
cd /dashboard</code></pre>
  </li>

  <li><strong>Crie e ative um ambiente virtual (opcional, mas recomendado):</strong>
    <pre><code>python3 -m venv venv
source venv/bin/activate   # Para Linux/MacOS
venv\Scripts\activate      # Para Windows</code></pre>
  </li>

  <li><strong>Instale as dependências:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li><strong>Execute a aplicação:</strong>
    <pre><code>python app.py </code></pre>
  </li>


</code></pre>
  </li>
</ul>
