import pandas as pd
import os
import random
import datetime as dt
import uuid
from .mysql_connections import ConexaoMysql
# from mysql_connections import ConexaoMysql


available_contexts = ['local','container','aws']

path_map = {
    'DATA_DIRECTORY':'DATA_DIRECTORY_CONTAINER',
    'TEMP_DIRECTORY':'TEMP_DIRECTORY_CONTAINER',
    'BACKUP_DIRECTORY':'BACKUP_DIRECTORY_CONTAINER'}

def checks_context(context:str):
    print(f"checks_context: {context} | log")

    if context not in available_contexts:
        raise Exception("Os modos permitidos são 'local','container','aws'.")
    else:
        pass
    return None

def checks_path(context:str):
    print(f"checks_path: {context} | log")
    available_contexts = path_map.keys()
    
    if context not in available_contexts:
        raise Exception("O caminho informado não consta no docker compose e no arquivo .env")
    else:
        pass
    return None

def maps_filepath(directory:str,mode='container'):
    checks_context(mode)
    checks_path(directory)    
    if mode == 'container':
        output_ = os.getenv(path_map[directory])
        print(output_)

    elif mode == 'local':
        output_ = os.getenv(directory)
        print(output_)
    else:
        pass
    return output_    

def retrieves_random_value_from_dataframe(dataframe: pd.DataFrame):
    return random.randint(1, len(dataframe) - 1)

def converter_datas(df):
    for coluna in list(df.columns)[:]:
        if coluna.startswith('data'):
            # Corrige o formato da data (substitui // por /)
            coluna = str(coluna)
            try:
                df[coluna] = pd.to_datetime(df[coluna].str.replace('//', '/'), errors='coerce')
            except:
                df[coluna] = df[coluna].astype('datetime64[ns]')
                print(f'A coluna {coluna} está no formato datetime64[ns]')
                pass
    return df

def reads_all_csv_files(path):
   
    print(f'## : {path} -- log #########')
    clientes_df = pd.read_csv(os.path.join(path,'clientes.csv'),sep=';',encoding='latin1')
    produtos_df = pd.read_csv(os.path.join(path,'produtos.csv'),sep=';',encoding='latin1')
    fornecedores_df = pd.read_csv(os.path.join(path,'fornecedor.csv'),sep=';',encoding='latin1')
    vendedores_df = pd.read_csv(os.path.join(path,'vendedores.csv'),sep=';',encoding='latin1')
    campanhas_df = pd.read_csv(os.path.join(path,'campanhas.csv'),sep=';',encoding='latin1')
    calendario_df = pd.read_csv(os.path.join(path,'calendario.csv'),sep=';',encoding='latin1')

    clientes_df = converter_datas(clientes_df)
    produtos_df = converter_datas(produtos_df)
    fornecedores_df = converter_datas(fornecedores_df)
    vendedores_df = converter_datas(vendedores_df)
    calendario_df = converter_datas(calendario_df)
    campanhas_df = converter_datas(campanhas_df)

    return clientes_df, produtos_df, fornecedores_df, vendedores_df, campanhas_df, calendario_df

def creates_sale_id():
    sale_registry = {'cod_venda':f'{random.randint(1,10000)}-{random.randint(99,999)}'}
    return sale_registry

def creates_sale_dictionary_key(starter_dictionary:dict,dataframe:pd.DataFrame,index_col:str):

    random_index = retrieves_random_value_from_dataframe(dataframe)
    starter_dictionary[str(index_col)] = int(dict(dataframe)[str(index_col)][random_index])
    return starter_dictionary

def creates_sales_registry(df_idx):
    sale_registry = creates_sale_id()
    for _ in range(1,5):
        sale_registry = creates_sale_dictionary_key(sale_registry,df_idx[_][0],df_idx[_][1])
    return sale_registry

def creates_cod_venda(df):
    # Função para gerar o UUID e atribuir ao grupo de cod_cliente
    def gerar_uuid():
        return uuid.uuid4().hex[:8]
    
    # Criar um dicionário para armazenar o UUID de cada grupo de cod_cliente
    uuid_dict = {}
    
    # Gerar UUIDs para cada grupo de 'cod_cliente'
    for cod_cliente in df['cod_cliente'].unique():
        uuid_dict[cod_cliente] = gerar_uuid()

    # Mapear o UUID para cada linha no DataFrame com base no cod_cliente
    df['cod_venda'] = df['cod_cliente'].map(uuid_dict)
    
    return df

def creates_sales_batch(path:str,batch_len=30,data_lote=None):
    clientes_df, produtos_df, fornecedores_df, vendedores_df, calendario_df, campanhas_df = reads_all_csv_files(path)
    df_idx = {
        1:[clientes_df,'cod_cliente'], 
        2:[produtos_df,'cod_produto'], 
        3:[fornecedores_df,'cod_fornecedor'], 
        4:[vendedores_df,'cod_vendedor']}

    if data_lote == None:
        data_lote = dt.datetime.today().strftime('%Y-%m-%d')
    else:
        data_lote = data_lote

    batch_id = uuid.uuid4().hex[:8]    

    sales_batch = {'lote_id':[],
                'data_venda':[],
                'cod_venda_unidade':[],
                'cod_cliente':[],
                'cod_produto':[],
                'cod_fornecedor':[],
                'cod_vendedor':[],
                'quantidade':[]}
    
    print(f'## creates_sales_batch log 1 {sales_batch}')

    for _ in range(1,batch_len):

        sale_registry = creates_sales_registry(df_idx)
        sales_batch['data_venda'].append(data_lote)
        sales_batch['lote_id'].append(batch_id)
        sales_batch['cod_venda_unidade'].append(uuid.uuid4().hex[:8])
        sales_batch['cod_cliente'].append(sale_registry['cod_cliente'])
        sales_batch['cod_produto'].append(sale_registry['cod_produto'])
        sales_batch['cod_fornecedor'].append(sale_registry['cod_fornecedor'])
        sales_batch['cod_vendedor'].append(sale_registry['cod_vendedor'])
        sales_batch['quantidade'].append(random.randint(1,4))
        print(f'## creates_sales_batch log 2 {pd.DataFrame(sales_batch)}')   
    
    print(f'## creates_sales_batch log 3 {sales_batch}')   

    return sales_batch

def creates_sales_dataframe(path:str,batch_len=30,data_lote=None):
    
    clientes_df, produtos_df, fornecedores_df, vendedores_df, calendario_df, campanhas_df = reads_all_csv_files(path)

    df_idx = {
        1:[clientes_df,'cod_cliente'], 
        2:[produtos_df,'cod_produto'], 
        3:[fornecedores_df,'cod_fornecedor'], 
        4:[vendedores_df,'cod_vendedor']}

    sale_registry = creates_sales_registry(df_idx)
    sales_batch = creates_sales_batch(path,random.randint(20,200),data_lote)

    sales_batch = pd.DataFrame(sales_batch)
    sales_batch = creates_cod_venda(sales_batch)
    
    print(f'## creates_sales_dataframe log 1 {sales_batch.columns}')
    return sales_batch

def mysql_connection_test():
    ConexaoMysql(connection_type='internal').create_engine()  

def insert_into_mysql(file_name:str,dataframe:pd.DataFrame):   
    
    cols = dataframe.columns
    cols = list(map(str.lower, cols))
    rows = []
    for linha in dataframe.itertuples(index=False, name=None):  # index=False para não incluir o índice na tupla
        rows.append(linha)

    ConexaoMysql(connection_type='internal').insert_into_from_dataframe(
        columns=cols, 
        rows=rows, 
        dst_database="my_database", 
        dst_table=file_name,
        insert_mode='ignore')



def sales_into_mysql(path:str,batch_len=30,data_lote=None):
    mysql_connection_test()
    
    dataframe = creates_sales_dataframe(path,batch_len,data_lote)
    insert_into_mysql('vendas_tb',dataframe)


def inserts_dim_tables_into_mysql(path:str,batch_len=30,data_lote=None):

    clientes_df, produtos_df, fornecedores_df, vendedores_df, campanhas_df, calendario_df  = reads_all_csv_files(path)
    df_idx = {
        1:[clientes_df,'clientes_tb'], 
        2:[produtos_df,'produtos_tb'], 
        3:[fornecedores_df,'fornecedores_tb'], 
        4:[vendedores_df,'vendedores_tb'],
        5:[calendario_df,'calendario_tb'],
        6:[campanhas_df,'campanhas_tb']
        }
    
    mysql_connection_test()

    for n in range(1,7):
        print(df_idx[n][1])
        print(df_idx[n][0])
        insert_into_mysql(df_idx[n][1],df_idx[n][0])

def creates_dates_range(data_inicio,data_fim):

    # Gerar a lista de datas
    datas = pd.date_range(start=data_inicio, end=data_fim).strftime('%Y-%m-%d').tolist()

    # Exibir a lista de datas
    return datas


# path = r'C:\Users\josec\Desktop\brasa_dados\local_airflow_python_mysql\source'

# creates_sales_batch(path)
# creates_sales_dataframe(path)
