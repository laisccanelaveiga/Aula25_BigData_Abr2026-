
import polars as pl 
from datetime import datetime


ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Carregando...')
    # Leitura Parquet *Preguiçosa
    # Métodos que geram plano de execução(.lazy() e scan_parquet())
    # lazy_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet').lazy() #- 0:00:17.469874
    lazy_bolsa_familia = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet') #0:00:03.792289
    # print(lazy_bolsa_familia) #Imprimindo o plano de execução

    lazy_bolsa_familia = lazy_bolsa_familia.select([
        'NOME MUNICÍPIO' , 'VALOR PARCELA'
    ])
    
    lazy_bolsa_familia = lazy_bolsa_familia.group_by(
        'NOME MUNICÍPIO'
    ).agg(
        pl.col('VALOR PARCELA').sum()
    )

    lazy_bolsa_familia = lazy_bolsa_familia.sort(by='VALOR PARCELA', descending=True)

    df_bolsa_familia = lazy_bolsa_familia.collect() #chamada dos dados

    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de Processamento: {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')