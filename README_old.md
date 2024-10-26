Projeto de Análise de Dados de Veículos

Este é um aplicativo web interativo desenvolvido com Streamlit, que permite explorar um conjunto de dados de anúncios de venda de carros. O objetivo do projeto é fornecer visualizações dinâmicas para entender melhor as variáveis dos dados de veículos, como odômetro (quilometragem) e preço.

Funcionalidades

Histograma: Visualize a distribuição da quilometragem dos veículos no conjunto de dados.

Gráfico de Dispersão: Explore a relação entre o preço e a quilometragem dos veículos.

Interatividade: O usuário pode selecionar as visualizações desejadas (histograma e/ou gráfico de dispersão) por meio de caixas de seleção.


Exemplo de Gráficos

Histograma

Exemplo de um histograma que mostra a distribuição da quilometragem (odometer).

Gráfico de Dispersão

Exemplo de um gráfico de dispersão que mostra a relação entre preço (price) e quilometragem (odometer).

Como Executar o Projeto Localmente

Pré-requisitos

Python 3.7 ou superior

As seguintes bibliotecas Python:

streamlit

pandas

plotly



Passos

1. Clone o repositório:

git clone https://github.com/seu-usuario/projeto-analise-de-dados-veiculos.git
cd projeto-analise-de-dados-veiculos


2. Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows


3. Instale as dependências:

pip install -r requirements.txt


4. Execute o aplicativo:

streamlit run app.py


5. O Streamlit abrirá automaticamente no navegador. Se isso não acontecer, acesse o endereço fornecido no terminal (geralmente http://localhost:8501).



Deploy no Render

Este projeto está configurado para funcionar no Render. Para isso, o arquivo de configuração do Streamlit (config.toml) foi adicionado com as definições de servidor necessárias.

Arquivo de Configuração do Streamlit (config.toml):

[server]
headless = true
port = 10000
enableCORS = false
[browser]
serverAddress = "0.0.0.0"
serverPort = 10000

Esse arquivo está localizado no diretório streamlit/config.toml e define as configurações do servidor para que o Render possa executar o aplicativo corretamente.

Estrutura do Projeto

projeto-analise-de-dados-veiculos/
│
├── streamlit/
│   └── config.toml       # Configurações do Streamlit para produção
├── app.py                # Código principal do aplicativo Streamlit
├── vehicles.csv          # Conjunto de dados de veículos
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo README

Conjunto de Dados

O conjunto de dados utilizado neste projeto (vehicles.csv) contém informações de anúncios de venda de veículos, incluindo:

Quilometragem (odometer)

Preço (price)

Marca, modelo e outras características dos veículos

README.md link (acesso ao aplicativo):
https://cabralprojrct-1.onrender.com
