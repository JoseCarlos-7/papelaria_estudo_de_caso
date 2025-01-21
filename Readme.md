
# Estudo de caso [Papelaria]

![apresentação](https://github.com/JoseCarlos-7/papelaria_estudo_de_caso/blob/main/imagens/header_.png)


![apresentação](https://github.com/JoseCarlos-7/papelaria_estudo_de_caso/blob/main/imagens/resumo%20arquitetura%20do%20projeto.png)

Este projeto oferece um exemplo de caso de integração de dados, utilizando Docker, MySQL, Python, Power BI e Airflow.
A arquitetura utiliza apenas infra local, e consiste em conteinerizar banco de dados my sql para armazenar os dados das transações e tabelas dimensão.

## Passos para rodar o projeto.
Clonar este repositório.

Após clonar o repositório, verificar se as seguintes pastas existem, se não, criá-las.
logs
config
plugins
backups

Editar o arquivo papelaria_estudo_de_caso\app\.env, ajustando o caminho das variáveis listadas abaixo.
.env

Ajustar .env inserindo o caminho das pastas source, temp e backups
DATA_DIRECTORY='C:\Users\josec\Desktop\dados2025\source'
TEMP_DIRECTORY='C:\Users\josec\Desktop\dados2025\temp'
BACKUP_DIRECTORY='C:\Users\josec\Desktop\dados2025\backups'

Acessar a pasta do projeto.
cd app
docker-compose -f airflow-docker-compose.yaml up -d

Acessar o Airflow.

http://127.0.0.1:8080

## Detalhamento do estudo



