import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
import math

def main():
    # adicionando link para download do arquivo
    st.markdown('Download do arquivo CSV: https://www.kaggle.com/datasets/samira1992/credit-card-data-intermediate-dataset ')

    # carregando arquivo csv
    data = pd.read_csv('datas/Customer_Data.csv')

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
    st.write('**Distribuição dos dados**')
    
    # Determinar o número de colunas e linhas para os subplots
    divisor = 4
    num_vars = len(data.columns)
    num_rows = math.ceil(num_vars / divisor)  # Altere o divisor para alterar o número de colunas

    fig, axs = plt.subplots(num_rows, divisor, figsize=(10, num_rows*5))

    for ax, column in zip(axs.flatten(), data.columns):
        sns.histplot(data[column], kde=True, ax=ax)

    # Remover subplots vazios
    if num_vars % 2 != 0:
        fig.delaxes(axs.flatten()[-1])

    st.pyplot(fig)
    plt.clf()

    #verificando a presença de outliers
    st.write('**Verificando a presença de outliers**')

    # Determinar o número de colunas e linhas para os subplots
    divisor = 4
    num_vars = len(data.columns)
    num_rows = math.ceil(num_vars / divisor)  # Altere o divisor para alterar o número de colunas

    fig, axs = plt.subplots(num_rows, divisor, figsize=(10, num_rows*5))
    for ax, column in zip(axs.flatten(), data.columns):
        sns.boxplot(y=data[column], ax=ax)

    # Remove empty subplots
    if num_vars % divisor != 0:
        fig.delaxes(axs.flatten()[-1])

    st.pyplot(fig)

if __name__ == '__main__': 
    main()