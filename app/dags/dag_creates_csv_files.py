from datetime import timedelta, datetime
# from functions.mysql_connections import ConexaoMysql
from functions.gerador_de_dados import maps_filepath,inserts_dim_tables_into_mysql
from functions.cria_calendario import saves_dataframe
from functions.ciar_dados_ficticios import saves_csv_files
from airflow import DAG #type: ignore
from airflow.operators.python import PythonOperator #type: ignore
from airflow.utils.dates import days_ago #type: ignore
from airflow.models import Param #type: ignore
from airflow.hooks.base import BaseHook #type: ignore
import datetime as dt
import sys
import os

default_args = {
    "owner": "JC",
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    dag_id="salvar_arquivos_csv",
    default_args=default_args,
    start_date=datetime(year=2025, month=1, day=1, hour=0),
    schedule_interval="0 12 5 * *",
    dagrun_timeout=timedelta(minutes=15),
    catchup=False,
    max_active_tasks=18

) as dag:     
          
    _maps_filepath = PythonOperator(
        task_id = f"checa_se_fonte_disponivel",
        python_callable=maps_filepath,
        op_kwargs={"directory":'DATA_DIRECTORY',"mode":'container'},
        provide_context=True,
        do_xcom_push=True
        )
    
    _saves_dataframe = PythonOperator(
        task_id = f"salva_arquivo_calendario_localmente",
        python_callable=saves_dataframe,
        op_kwargs={"path":"{{task_instance.xcom_pull(task_ids='checa_se_fonte_disponivel', key='return_value')}}"}
        )
    
    _saves_csv_files = PythonOperator(
        task_id = f"salva_arquivos_dim_localmente",
        python_callable=saves_csv_files,
        op_kwargs={"path":"{{task_instance.xcom_pull(task_ids='checa_se_fonte_disponivel', key='return_value')}}"}
        )
    
    _maps_filepath >> [_saves_dataframe , _saves_csv_files]