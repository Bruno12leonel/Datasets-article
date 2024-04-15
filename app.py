import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns



def main():
    # adicionando link para download do arquivo
    st.markdown('Download do arquivo CSV: https://www.kaggle.com/datasets/samira1992/credit-card-data-intermediate-dataset ')

    # carregando arquivo csv
    data = pd.read_csv('Customer_Data.csv')

    # mostrando informação de dimensionamento dos dados em formato de tabela
    st.write('**Dimensão dos dados**')

    # fazendo uma tabela com as dimensões dos dados
    st.write('Linhas: ', data.shape[0])
    st.write('Colunas: ', data.shape[1])

    # adicionando texto de legenda
    st.write('**Visualizando os dados antes de tratar**')
    st.write(data.head())

    # removendo primeira coluna 'CUST_ID'
    data = data.drop('CUST_ID', axis=1)
    
    # mostrando dados sem a coluna 'CUST_ID'
    st.write('**Drop da coluna `CUST_ID`**')
    st.write(data.head())

    #mostrando correlação entre as variáveis
    st.write('**Correlação entre as variáveis**')
    st.write(data.corr())

    # verificando ausensia de valores NaN
    st.write('**Verificando valores NaN**')
    st.write(data.isnull().sum())

    # completando dados NaN com a média
    data.fillna(data.mean(), inplace=True)

    # Mostrando dados depois de preencher com a media
    st.write('**Dados depois de preencher os valores NaN com a média da coluna**')
    st.write(data.head())  

    # verificando ausensia de valores NaN
    st.write('**Verificando valores NaN**')
    st.write(data.isnull().sum())


    #plotando gráfico de correlação
    st.write('**Gráfico de correlação**')

    # plot do grafico de correlação
    st.line_chart(data.corr())


    # Visualizando dados utlizando PCA
    st.write('**Visualizando dados utilizando PCA**')
    pca = PCA(n_components = 2)
    data_pca = pca.fit_transform(data)

    # plotando os dados utilizando matplotlib no streamlit
    fig, ax = plt.subplots()
    ax.scatter(data_pca[:, 0], data_pca[:, 1], c='black')
    st.pyplot(fig)

    # Verificando a distribuição dos dados
    for column in data.columns:
        fig, ax = plt.subplots()
        sns.histplot(data[column], kde=True)

        # adicionando titulo ao gráfico
        plt.title(f'Distribuição de {column}')

        st.pyplot(fig)
        plt.clf()



if __name__ == '__main__': 
    main()
