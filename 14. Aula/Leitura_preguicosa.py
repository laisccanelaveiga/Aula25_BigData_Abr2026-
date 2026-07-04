
import polars as pl 
from datetime import datetime


ENDERECO_DADOS = './../DADOS/bolsa_familia/'

try:
    # Leitura Preguiçosa scan_parquet
    # Scan_parquet gera um plano de execução, não trás o dados de imediato
    inicio = datetime.now()
    print('Carregando...')

    df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    # print(df_scan) #printando o plano de execução

    # Pré Processamento (organizar dados)
    ...

    # Collect executa o plano carregando os dados p/ a memória
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())
    
    final = datetime.now()
    print(f'Tempo de Processamento: {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet: {e}')
