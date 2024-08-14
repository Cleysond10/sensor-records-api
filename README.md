# API de Registros de Sensores

Este projeto é uma API Python, desenvolvida com FastAPI, é responsável por coletar dados de sensores em tempo real e armazená-los em um banco de dados.

## Funcionalidades:

- Registrar leituras de sensores em banco de dados relacional.
- Poder subir um arquivo CSV para inserir múltiplos registros.

## Tecnologias Utilizadas:

- FastAPI
- Python
- MySQL Database

## Pré-requisitos:

- Python
- Git
- Um ambiente virtual (recomendado)

## Instalação e Execução:

- Clone o repositório:
`git clone https://github.com/Cleysond10/sensor-records-api.git`

- Navegue para o diretório do projeto:
`cd sensor-records-api`

- Crie o ambiente virtual
`python -m venv env`

- [WINDOWS] Ative o ambiente virtual no Windows
`.\env\Scripts\activate`

- [LINUX/MACOS] Ative o ambiente virtual no Linux ou MacOS
`source ./env/bin/activate`

- Certifique-se de ter o pacote pip instalado
`python -m pip install --upgrade pip`

- Instale as dependências:
`pip install -r requirements.txt`

- Inicie o servidor de desenvolvimento:
`fastapi dev`

- Acesse a documentação da api no seu navegador em http://localhost:8000/docs.


## Autor:

@Cleysond10
