from datetime import datetime
import os
from subprocess import Popen, PIPE
import traceback
from sqlalchemy import create_engine #type: ignore


class ConexaoMysql():

    def __init__(self, connection_type: str, connection_data: dict={"username":"","password":"","host":"","port":""}):

        try:

            conn_allowed_types = ["internal", "external","custom"]
                
            if connection_type not in conn_allowed_types:
                raise ValueError("Err: O parâmetro deve ser 'internal', 'external' ou 'custom'.")
            
            if connection_type == "custom" and connection_data =={"username":"","password":"","host":"","port":""}:
                raise ValueError("Err: É necessário informar os dados da conexão quando o parâmetro for 'custom'.")
            
            if connection_type=="internal":

                self.username = os.environ.get('MYSQL_USER_INT')
                self.password = os.environ.get('MYSQL_PASSWORD_INT')
                self.host = os.environ.get('MYSQL_HOST_INT')
                self.port = os.environ.get('MYSQL_PORT_INT')

            elif connection_type=="external":

                self.username = os.environ.get('MYSQL_USER_EXT')
                self.password = os.environ.get('MYSQL_PASSWORD_EXT')
                self.host = os.environ.get('MYSQL_HOST_EXT')
                self.port = os.environ.get('MYSQL_PORT_EXT')

            elif connection_type=="custom":

                self.username = connection_data["username"]
                self.password = connection_data["password"]
                self.host = connection_data["host"]
                self.port = connection_data["port"]

            self.path_load_infile = os.environ.get('TEMP_DIRECTORY')
            self.path_backup = os.environ.get('BACKUP_DIRECTORY')
            
        except ValueError as err:
            
            print(err, type(err), traceback.format_exc())
            raise

        except Exception as err:
            
            print(err, type(err), traceback.format_exc())
            raise       

    def create_engine(self) -> object:

        try:            
            username = self.username
            password = self.password
            host = self.host
            port = self.port
            
            engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}',pool_size=20, max_overflow=0)#,isolation_level="AUTOCOMMIT")
            
            return engine

        except Exception as err:
            print('Erro na conexão.')
            print(err, type(err), traceback.format_exc())
            raise

    def insert_into_from_dataframe(self, columns: list, rows: list, dst_database: str, dst_table: str, insert_mode: str=""):

        try:
            
            allowed_types = ["", "ignore"]

            if insert_mode not in allowed_types:
                raise ValueError("Err: O parâmetro deve ser 'ignore' ou não informado.")
            
            flag = self.verify_table(dst_database, dst_table)

            if flag == 0:
                raise ValueError(f"Err: A tabela especificada {dst_table} não existe, é necessário criá-la primeiro.")

            columns_insert = ','.join([column for column in columns])  
            param_values = ','.join(['%s' for column in columns])

            if insert_mode == "ignore":

                query = f"INSERT IGNORE INTO {dst_database}.{dst_table}({columns_insert}) VALUES ({param_values})"

            else:                

                query = f"INSERT INTO {dst_database}.{dst_table}({columns_insert}) VALUES ({param_values})"

            if len(rows) !=0:

                with self.create_engine().connect() as conn:
                    conn.execute(query,rows)

            return print(f"Linhas inseridas com sucesso. ## {dst_table} ##")
        
        except ValueError as err:
            
            print(err, type(err), traceback.format_exc())
            raise

        except Exception as err:
            
            print(err, type(err), traceback.format_exc())
            raise   
        
    
    def verify_table(self, database: str, table_name: str):

        try:

            flag = 1

            query = f"SELECT * FROM information_schema.tables WHERE table_schema = '{database}' AND table_name = '{table_name}' LIMIT 1;"

            with self.create_engine().connect() as conn:
                result = conn.execute(query).fetchone()

            if result is None:
                
                flag = 0

            return flag

        except Exception as err:
            
            print(err, type(err), traceback.format_exc())
            raise   

