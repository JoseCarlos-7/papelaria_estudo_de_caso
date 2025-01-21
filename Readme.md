
# Estudo de caso [Papelaria]

![apresentação](https://github.com/JoseCarlos-7/papelaria_estudo_de_caso/blob/main/imagens/header_.png)


![apresentação](https://github.com/JoseCarlos-7/papelaria_estudo_de_caso/blob/main/imagens/resumo%20arquitetura%20do%20projeto.png)

Este projeto oferece um exemplo de caso de integração de dados, utilizando Docker, MySQL, Python, Power BI e Airflow.
A arquitetura utiliza apenas infra local, e consiste em conteinerizar banco de dados my sql para armazenar os dados das transações e tabelas dimensão. <br>

**Requisitos** <br>
Para executar o projeto é necessário ter instalado Power Bi, Docker, IDE (Aqui utilizei VS Code) e algum client MySQL (Aqui usei Workbench). Todos esses aplicativos tem opção gratuita.

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

## SQL
Antes de executar as tasks de armazenamento de dados, é fundamental criar as tabelas no banco de dados. Os scripts de criação das tabelas estão no diretório ***sql***. Você pode executá-los utilizando o client SQL de sua preferência. Aqui utilizei o Workbench.

Pacotes e funções mais importantes:

## criação de dados

**ciar_dados_ficticios**

creates_dictionaries(): Retorna um dicionário de listas em que o primeiro elemento da lista é um dicionário com dados fictícios de uma 
entidade, e o segundo elemento é o nome do arquivo a ser salvo em formato CVS.

saves_csv_files(): Salva os dicionários em formato cvs.

**cria_calendario**
saves_dataframe(): Função que salva um calendário em formato csv, que será usado como dimensão calendário no Power BI.

## Armazenamento no MySql

**gerador_de_dados**
reads_all_csv_files(path): Faz a leitura dos arquivos CSV salvos após a criação. <br>
inserts_dim_tables_into_mysql(): Insere as tabelas de dimensão no MySql. <br>
sales_into_mysql(): Lê as tabelas de dimensão e utiliza as chaves primárias para criar uma tabela de transações (fato) com chaves estrangeiras relacionadas a cada entidade. <br>

## Orquestração
Para todas as tasks de orquestração, é muito importante que o arquivo .env receba o caminho correto da pasta source da máquina local. Existe a função que checa o caminho e retorna mensagem de log caso esteja incorreta.

**dag_creates_csv_files**
maps_filepath(): checa se o diretório informado para salvar os arquivos está presente no .env, passa como variável para as seguintes tasks:
task_id = f"salva_arquivo_calendario_localmente"
task_id = f"salva_arquivos_dim_localmente"

**dag_dim_tables**
maps_filepath(): checa se o diretório informado para salvar os arquivos está presente no .env, passa como variável para as seguintes tasks:
task_id = f"carga_das_tabelas_dim"

**dag_transactions**
maps_filepath(): checa se o diretório informado para salvar os arquivos está presente no .env, passa como variável para as seguintes tasks:
task_id = f"carga_do_lote_de_vendas"

## Power Bi
Após a execução de todas as tasks, é possível acessar os dados armazenados no MySql via Power Bi. O banco de dados é servido no 127.0.0.1 e banco de dados my_database.
O arquivo disponível já está configurado para as conexões funcionarem e os dados apresentados. 








