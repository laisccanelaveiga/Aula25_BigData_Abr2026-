# import pandas as pd 
import polars as pl
from datetime import datetime 
import os 

ENDERECO_DADOS = './../DADOS/bolsa_familia/'

try:
    inicio = datetime.now()
    print('Carregando...')
    
    lista_dir_arquivo = os.listdir(ENDERECO_DADOS)

    df_bolsa_familia = None
    lista_arquivos = []
    
    for arquivo in lista_dir_arquivo:
        if arquivo.endswith('.csv'):
            lista_arquivos.append(arquivo)
    
    for nome in lista_arquivos:
        print(f'\nProcessando o arquivo {nome}')
        
        # Com Pandas: 0:04:16.448792
        # Com Polars: 0:00:36.477346

        # df = pd.read_csv(ENDERECO_DADOS + nome, sep=";", encoding='iso-8859-1')
        df = pl.read_csv(ENDERECO_DADOS + nome, separator=";", encoding='iso-8859-1')
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            # df_bolsa_familia = pd.concat([df_bolsa_familia, df])
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])

        del df

        print(f'Arquivo {nome} processado com sucesso!')
    #     print(df_bolsa_familia.head())
            
    
    # Próximo passo - Tratamento de Dados.
    # Valor parcela está com vígula e ele precisa ter ponto para ser reconhecido como int ou float
    df_bolsa_familia = df_bolsa_familia.with_columns(
        pl.col('VALOR PARCELA').str.replace(',', '.').cast(pl.Float64)
    )


    print('\nIniciando a gravação do arquivo parquet...')
    df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    print('\nGravação do arquivo parquet concluído com sucesso!')

    print(f'{df_bolsa_familia.shape}')
    print(df_bolsa_familia.columns)
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de Processamento: {final - inicio}')

        
except Exception as e:
    print(f'Erro ao carregar dados: {e}')


