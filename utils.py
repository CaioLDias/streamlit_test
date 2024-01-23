from dataset import df
import pandas as pd
import streamlit as st
import time

#formata o numero de acordo com a condição if, somando o prefixo programado no app.py
def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

#CRIA UM DATAFRAME CHAMADO REC_ESTADO (DATAFRAME É UMA TABELA NOVA)
##agrupa pela somatoria do preço e pelo estado da coluna local da compra
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
##remove registros duplicados da coluna subset local da compra
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat','lon']].merge(df_rec_estado,left_on='Local da compra',right_index=True).sort_values('Preço',ascending=False)

#DATAFRAME RECEITA MENSAL
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
##Cria uma coluna formatada com as informações de ano da coluna data da compra
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
##Cria uma coluna formatada com as informações de mês da coluna data da compra
df_rec_mensal['Mês'] = df_rec_mensal['Data da Compra'].dt.month_name()

#DATAFRAME RECEITA POR CATEGORIA
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending = False)

#DATAFRAME DE VENDEDORES
###df_vendedores = df.groupby('Vendedores')[['Preço']].sum().sort_values('Preço', ascending = False)
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))

#Função para converter arquivo .csv
@st.cache_data
def convert_csv(df):
    return df.to_csv(index = False).encode('utf-8')
#mostra mensagem de sucesso no download
def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon = '✔️'
        )
    time.sleep(3)
    success.empty()