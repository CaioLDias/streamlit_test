import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

#cria o titulo e o filtro de colunas
st.title('Dataset de Vendas')
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as colunas',
        list (df.columns),
        list (df.columns)
        )

#cria a sidebar na esquerda de filtros
st.sidebar.title('Filtros')
##filtro categoria do produto
with st.sidebar.expander('Categoria do produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
    )
##filtro preço do produto
with st.sidebar.expander('Preço do produto'):
    preco = st.slider(
        'Selecione o preço',
        0, 5000,
        (0, 5000)
        )
##filtro data da compra
with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),
        df['Data da Compra'].max())
    )

#na query, a crase faz referencia a uma coluna em especifico, barra invertida pra pular de linha, coluna numerica nao coloca crase
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
##filtra linhas (shape[0])
filtro_dados = df.query(query)
##filtra colunas (shape[1])
filtro_dados = filtro_dados[colunas]

#mostra o dataframe de acordo com a query de filtro de dados
st.dataframe(filtro_dados)

#mostra quantas linhas e quantas colunas o dataset possui, shape 0 e shape 1
st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

#funçao para fazer o download do arquivo
st.markdown('Escreva o nome do arquivo')

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility = 'collapsed'
    )
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar arquivo',
        data = convert_csv(filtro_dados),
        file_name = nome_arquivo,
        mime = 'text/csv',
        on_click = mensagem_sucesso
    )
