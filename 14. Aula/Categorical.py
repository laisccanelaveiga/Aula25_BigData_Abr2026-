import polars as pl 
from datetime import datetime


ENDERECO_DADOS = './../DADOS/bolsa_familia/'

try:
    inicio = datetime.now()
    print('Carregando...')
    # Uso do Categorical para maximizar a performance da RAM
    # Uso do Categorical para comparar os municípios repetidos
    df_scan = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        .select(['NOME MUNICÍPIO' , 'VALOR PARCELA'])
        .with_columns([
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
        ])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort('VALOR PARCELA', descending=True)
    )

    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de Processamento: {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')