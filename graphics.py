import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

#CRIA UM GRAFICO DE MAPA
grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)

#CRIA UM GRAFICO DE LINHAS
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mês',
    y = 'Preço',
    markers = True,
    range_y = (0,df_rec_mensal.max()),
    color = 'Ano',
    line_dash = 'Ano',
    title = 'Receita Mensal'
)
##atualiza o nome do eixo y para Receita
grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

#CRIA UM GRAFICO DE BARRAS
grafico_rec_estado = px.bar(
    df_rec_estado.head(10),
    x = 'Local da compra',
    y = 'Preço',
    text_auto = True,
    title = 'Top receita por estados'
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto = True,
    title = 'Top 7 categorias com maior receita'
)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending = False).head(7),
    x = 'sum',
    y = df_vendedores[['sum']].sort_values('sum', ascending = False).head(7).index,
    text_auto = True,
    title = 'Top 7 vendedores por receita'
)

grafico_venda_vendedores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending = False).head(7),
    x = 'count',
    y = df_vendedores[['count']].sort_values('count', ascending = False).head(7).index,
    text_auto = True,
    title = 'Top 7 vendedores por quantidade de vendas'
)

