import requests
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import wordcloud
import logging
import schedule
import time


import warnings
warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

csv_path = '/Users/anapaulaferes/Desktop/Curso/Tokens e Chaves/govbr.csv'
df_token = pd.read_csv(csv_path)
token_value = df_token.loc[0, 'value']
headers = {"chave-api-dados": token_value}


def run_request(url_):
    resposta = requests.get(url_, headers=headers)
    return resposta.json()


def coletar_dados(url):
    logging.info('Pegou url para a criação das diferentes URLs criando uma para cada página')
    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
    list_urls = [url + str(i) for i in range (1, 6)] #alterei de 409 para ser mais rápido
    arr_urls = np.asarray(list_urls)

    vec_run = np.vectorize(run_request)
    logging.info('Fazendo uma requisição para cada URL...')
    arr_responses = vec_run(arr_urls)
    logging.info('Requisições concluídas')
    arr_responses = arr_responses.tolist()
    resposta = np.concatenate(arr_responses).tolist()
    df = pd.DataFrame(resposta)
    return resposta


def transformar_dado(dado):
    logging.info('Criando dataframe')
    df = pd.DataFrame(dado)

    logging.info('Selecionando colunas')
    df_area = df[['funcao', 'valorEmpenhado']]

    logging.info('Transformando dado string -> float')
    df_area['valorEmpenhado'] = df_area['valorEmpenhado'].str.replace('.', '').str.replace(',', '.').astype(np.float32)
    agg_area = df_area.groupby('funcao').sum('valorEmpenhado')
    
    logging.info('Transformando dados para retirar proporção em porcentagem')
    agg_area = agg_area['valorEmpenhado']/df_area['valorEmpenhado'].sum()
    agg_area = agg_area.reset_index()
    return agg_area

def carga(dado):
    logging.info('Salvando arquivo...')
    dado.to_csv('distribuicao_empenho_area_2022', index=True)
    logging.info('Arquivo salvo')


def etl():
    logging.info('ETL iniciada...')

    url = 'https://api.portaldatransparencia.gov.br/api-de-dados/emendas?ano=2022&pagina='
    dado = coletar_dados(url)
    dado = transformar_dado(dado)
    carga(dado)
    logging.info('ETL finalizada.')


# etl()

# Automação

schedule.every().day.at('04:00').do(etl)

while True:
    schedule.run_pending()
    time.sleep(3600)
    