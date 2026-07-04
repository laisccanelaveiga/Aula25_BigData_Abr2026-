
# pip install fastparque - Precisoinstalar com o pandas
# import pandas as pd
import polars as pl 
from datetime import datetime


ENDERECO_DADOS = './../DADOS/bolsa_familia/'

try:
    # Lendo parquet - Leitura Direta
    inicio = datetime.now()
    print('Carregando...')

    # Pandas: 0:00:29.444928
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # Polars: 0:00:08.348070
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    print(df_bolsa_familia.head())

    # Leitura Não Direta
    final = datetime.now()
    print(f'Tempo de Processamento: {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')

