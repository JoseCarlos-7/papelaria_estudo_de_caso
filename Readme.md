
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

## Panorama do estudo.
Uma maneira simples de entender o panorama é observá-lo em três partes distintas:

1 - Geração de dados fictícios: Dentro da pasta functions, temos pacotes destinados exclusivamente para a criação de dados como, nomes de clientes, fornecedores, produtos, calendario e vendedores.
Os pacotes são:
***app\dags\functions\ciar_dados_ficticios.py***
***app\dags\functions\cria_calendario.py***
O objetivo principal desses pacotes é gerar dicionários com dados fictícios, convertê-los em Pandas Dataframe e salvá-los em formato CSV localmente dentro do diretório ***source***. <br>

2 - Armazenamento dos dados gerados: Dentro da pasta functions, existe o pacote ***app\dags\functions\gerador_de_dados.py***. O objetivo dele é ler os arquivos CSV recém gerados e armazená-los em banco MySql. <br>

3 - Orquestração: A orquestração é feita pelo Apache Airflow, que executa as funções de geração de dados e armazenamento de forma agendada. O diretório ***dags*** contém os arquivos que armazenam os scripts de orquestração. Lá você encontra três DAGs <br>
app\dags\dag_creates_csv_files.py
app\dags\dag_dim_tables.py
app\dags\dag_transactions.py <br>

4 - Visualização em Dashboard: Uma vez que os dados estejam armazenados no banco de dados, estes ficam disponíveis para visualização em Power Bi. O diretório ***power_bi*** contém um arquivo pbix que pode ser baixado para visualização e customização.

## Detalhamento do estudo

Como todos os dados utilizados para este estudo são fictícios,





