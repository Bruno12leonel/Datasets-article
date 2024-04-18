
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA



def main():
    # adicionando link para download
    st.markdown('Download do arquivo CSV: https://archive.ics.uci.edu/dataset/221/kegg+metabolic+reaction+network+undirected')

    # carregando arquivo csv
    data = pd.read_csv('datas/reaction_network.csv', sep=',')

    # mostrando informação de dimensionamento dos dados em formato de tabela
    with st.expander('**Dimensão dos dados**'):
        # fazendo uma tabela com as dimensões dos dados
        st.write('Linhas: ', data.shape[0])
        st.write('Colunas: ', data.shape[1])

    # texto explicando que o dataset não tinha nome para as colunas logo coloquei nomes aleatórios
    with st.expander('Nome das colunas'):
        st.write('As colunas não possuem nome, logo coloquei nomes aleatórios')

    # adicionando texto de legenda
    with st.expander('**Visualizando os dados antes de tratar**'):
        st.write(data.head())


    # mostrando nome das colunas e tipo de dados
    with st.expander('**Nome das colunas e tipo de dados**'):
        st.write(data.dtypes)


    # dropando coluna 'ID'
    with st.expander('Drop da coluna ID'):
        st.write('dropando coluna ID uma vez que não é relevante para a análise')
        data = data.drop('ID', axis=1)
        st.write(data.head())

    #verificando se há valores com strings
    with st.expander('**Verificando se há valores com strings**'):
        st.write(data.applymap(type).eq(str).any())
        st.write('Há valores com strings, logo é necessário fazer a conversão para numérico')

    #convertendo valores para numérico
    with st.expander('**Convertendo valores para numérico**'):
        data = data.apply(pd.to_numeric, errors='coerce')
        st.write(data.dtypes)

    #verificando se há valores com strings novamente
    with st.expander('**Verificando se há valores com strings**'):
        st.write(data.applymap(type).eq(str).any())

    #verificando valores NaN
    with st.expander('**Verificando valores NaN**'):
        st.write(data.isnull().sum())
        st.write('Há valores NaN, logo é necessário preencher com a média')
    
    # preenchendo valores NaN com a média
    with st.expander('**Preenchendo valores NaN com a média**'):
        data.fillna(data.mean(), inplace=True)
        st.write(data.isnull().sum())
    
    #plotando gráfico de correlação
    with st.expander('**Gráfico de correlação**'):
        st.line_chart(data.corr())

    # Visualizando dados utlizando PCA
    with st.expander('**Visualizando dados utilizando PCA**'):
        pca = PCA(n_components = 2)
        data_pca = pca.fit_transform(data)

        # plotando os dados utilizando matplotlib no streamlit
        fig, ax = plt.subplots()
        ax.scatter(data_pca[:, 0], data_pca[:, 1], c='black')
        st.pyplot(fig)

    # Verificando a distribuição dos dados
    with st.expander('**Distribuição dos dados**'):
        # Determinar o número de colunas e linhas para os subplots
        divisor = 4
        num_vars = len(data.columns)
        fig, ax = plt.subplots(num_vars // divisor + 1, divisor, figsize=(20, 20))
        for i, var in enumerate(data.columns):
            ax[i // divisor, i % divisor].hist(data[var])
            ax[i // divisor, i % divisor].set_title(var)
        st.pyplot(fig)
    
    # verificando se há outliers
    with st.expander('**Verificando se há outliers**'):
        fig, ax = plt.subplots(num_vars // divisor + 1, divisor, figsize=(20, 20))
        for i, var in enumerate(data.columns):
            ax[i // divisor, i % divisor].boxplot(data[var])
            ax[i // divisor, i % divisor].set_title(var)
        st.pyplot(fig)

    # Conclusão do que eu fiz nos dados para poder trabalhar com eles
    st.write('**Resumo das operações realizadas**')
    st.write('1. Drop da coluna ID')
    st.write('2. Convertendo valores para numérico')
    st.write('3. Preenchendo valores NaN com a média')
    st.write('4. Visualizando os dados utilizando PCA')
    st.write('5. Verificando a distribuição dos dados')
    st.write('6. Verificando a presença de outliers')

    # Texto de conclusão
    st.write('**Conclusão**')
    st.write('Os dados estavam com valores NaN e strings, logo foi necessário fazer a conversão para numérico e preencher os valores NaN com a média. Após isso, foi possível visualizar os dados utilizando PCA e verificar a distribuição dos dados e a presença de outliers.')
    
    # Adicionando botão para download do arquivo
    st.markdown('**Download do arquivo tratado:**')
    st.markdown('Clique no botão abaixo para baixar o arquivo CSV final')
    st.markdown('**[Download do arquivo CSV](https://drive.google.com/file/d/11XhQeMMxDqDRkdUGYv6aT9powdk8Wnuu/view?usp=sharing)**')



if __name__ == '__main__': 
    main()