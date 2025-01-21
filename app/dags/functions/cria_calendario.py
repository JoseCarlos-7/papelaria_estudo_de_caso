

# from .mysql_connections import ConexaoMysql
import pandas as pd
import numpy as np
import os
# from pandas.tseries.offsets import BDay

feriados = ['2023-12-25','2023-11-15','2023-11-02','2024-01-01','2024-02-12','2024-02-13','2024-03-29','2024-04-08','2024-04-21','2024-05-01','2024-05-30','2024-05-31','2024-09-07','2024-10-12','2024-10-28','2024-11-02','2024-11-15','2024-11-20','2024-12-25',
            '2025-01-01','2025-04-18','2025-04-21','2025-05-01','2025-09-07','2025-10-12','2025-11-02','2025-11-15','2025-11-20','2025-12-25']

# Função para calcular o quinto dia útil anterior
def dia_util_anterior(data, ndias,feriados):
    date = pd.to_datetime(data)
    count = 0
    while count < ndias:
        date -= pd.Timedelta(days=1)
        # Pular sábados (6) e domingos (7), ou se for feriado
        if date.weekday() < 5 and date.strftime('%Y-%m-%d') not in feriados:  # Segunda a Sexta e não é feriado
            count += 1
    return date.strftime('%Y-%m-%d')

# Função para calcular o quinto dia útil anterior
def dia_util_posterior(data, ndias,feriados):
    date = pd.to_datetime(data)
    count = 0
    while count < ndias:
        date += pd.Timedelta(days=1)
        # Pular sábados (6) e domingos (7), ou se for feriado
        if date.weekday() < 5 and date.strftime('%Y-%m-%d') not in feriados:  # Segunda a Sexta e não é feriado
            count += 1
    return date.strftime('%Y-%m-%d')


# Função para calcular os períodos (45, 30, 15 dias)
def calcular_periodos(data):
    data = pd.to_datetime(data)
    periodo_45_antes = (data - pd.DateOffset(days=45)).strftime('%y/%m/%d')
    periodo_45_depois = (data + pd.DateOffset(days=45)).strftime('%y/%m/%d')
    
    periodo_30_antes = (data - pd.DateOffset(days=30)).strftime('%y/%m/%d')
    periodo_30_depois = (data + pd.DateOffset(days=30)).strftime('%y/%m/%d')
    
    periodo_15_antes = (data - pd.DateOffset(days=15)).strftime('%y/%m/%d')
    periodo_15_depois = (data + pd.DateOffset(days=15)).strftime('%y/%m/%d')
    
    return periodo_45_antes, periodo_45_depois, periodo_30_antes, periodo_30_depois, periodo_15_antes, periodo_15_depois


# Função para determinar o nome do mês
def nome_mes(mes):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    return meses[mes - 1]

# Função para determinar o mês abreviado
def nome_mes_abreviado(mes):
    meses_abrev = ['jan', 'fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    return meses_abrev[mes - 1]

def saves_dataframe(path):
    # Gerar a sequência de datas
    datas = pd.date_range(start="2024-01-01", end="2025-12-31", freq='D')

    # Criar o DataFrame para o calendário
    calendario = pd.DataFrame(datas, columns=['data'])

    # Calcular os períodos de 45, 30, 15 dias
    calendario[['periodo_45_antes', 'periodo_45_depois', 'periodo_30_antes', 'periodo_30_depois', 'periodo_15_antes', 'periodo_15_depois']] = calendario['data'].apply(
        lambda x: pd.Series(calcular_periodos(x)))


    # Calcular o décimo dia útil anterior
    calendario['decimo_dia_util_anterior'] = calendario['data'].apply(lambda x: dia_util_anterior(x, 9,feriados[:]))

    # Calcular o quinto dia útil anterior
    calendario['quinto_dia_util_anterior'] = calendario['data'].apply(lambda x: dia_util_anterior(x, 4,feriados[:]))

    # Calcular o quinto dia útil anterior
    calendario['segundo_dia_util_anterior'] = calendario['data'].apply(lambda x: dia_util_anterior(x, 1,feriados[:]))


    # Calcular o décimo dia útil posterior
    calendario['decimo_dia_util_posterior'] = calendario['data'].apply(lambda x: dia_util_posterior(x, 9,feriados[:]))

    # Calcular o quinto dia útil posterior
    calendario['quinto_dia_util_posterior'] = calendario['data'].apply(lambda x: dia_util_posterior(x, 4,feriados[:]))

    # Calcular o quinto dia útil posterior
    calendario['segundo_dia_util_posterior'] = calendario['data'].apply(lambda x: dia_util_posterior(x, 1,feriados[:]))


    # Adicionar a coluna "quinzena" com base no dia do mês
    calendario['quinzena'] = np.where(calendario['data'].dt.day <= 15, 'primeira_quinzena', 'segunda_quinzena')

    # Adicionar o nome do mês
    calendario['nome_mes'] = calendario['data'].dt.month.apply(nome_mes)

    # Adicionar o nome abreviado do mês
    calendario['nome_mes_abreviado'] = calendario['data'].dt.month.apply(nome_mes_abreviado)

    # Adicionar o número do dia do mês
    calendario['dia_do_mes'] = calendario['data'].dt.day

    # Adicionar o número do dia da semana
    calendario['numero_dia_da_semana'] = calendario['data'].dt.weekday + 1  # Segunda = 1, Domingo = 7

    # Adicionar o nome do dia da semana
    calendario['dia_da_semana'] = calendario['data'].dt.strftime('%A')

    # Adicionar a abreviação do dia da semana
    calendario['dia_da_semana_abreviado'] = calendario['data'].dt.strftime('%a')

    # Adicionar o número do dia do ano
    calendario['dia_do_ano'] = calendario['data'].dt.dayofyear

    # Adicionar o ano
    calendario['ano'] = calendario['data'].dt.year

    #adiciona pk
    calendario['pk_dates'] = range(1, len(calendario) + 1)

    # adiciona mes
    calendario['mes'] = calendario['data'].dt.month

    calendario['periodo_15_dias_ate_data'] = 'de ' + pd.to_datetime(calendario['periodo_15_antes']).dt.strftime('%y/%m/%d') + ' a ' + calendario['data'].dt.strftime('%y/%m/%d')
    calendario['periodo_30_dias_ate_data'] = 'de ' + pd.to_datetime(calendario['periodo_30_antes']).dt.strftime('%y/%m/%d') + ' a ' + calendario['data'].dt.strftime('%y/%m/%d')
    calendario['periodo_45_dias_ate_data'] = 'de ' + pd.to_datetime(calendario['periodo_45_antes']).dt.strftime('%y/%m/%d') + ' a ' + calendario['data'].dt.strftime('%y/%m/%d')

    # Gerar a tabela com os períodos
    calendario_final = calendario[[
    'data',
    'dia_da_semana', 
    'mes',
    'nome_mes', 
    'periodo_30_dias_ate_data',
    'periodo_30_antes', 
    'periodo_30_depois'
    ]
    ]
    calendario_final.to_csv(os.path.join(path,'calendario.csv'),encoding='latin1',sep=';',index=None)
    return None

# saves_dataframe(r'C:\Users\josec\Desktop\projeto_subir\papelaria_estudo_de_caso\source')

