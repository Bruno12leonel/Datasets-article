import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
def main():

    # adicionando link para download
    st.markdown('Download do arquivo CSV: https://archive.ics.uci.edu/dataset/551/gas+turbine+co+and+nox+emission+data+set')

    # carregando arquivo csv
    data = pd.read_csv('datas/gas_turbine_co_and_nox_emission_data_set.csv', sep=',')

    # mostrando informação de dimensionamento dos dados em formato de tabela
    with st.expander('**Dimensão dos dados**'):
        # fazendo uma tabela com as dimensões dos dados
        st.write('Linhas: ', data.shape[0])
        st.write('Colunas: ', data.shape[1])

    # visualizando os dados
    with st.expander('**Visualizando os dados antes de tratar**'):
        st.write(data.head())
    
    # texto explicando que a coluna 'year' não é um atributo relevante para análiso logo será dropada
    with st.expander('Drop da coluna "year"'):
        st.write('dropando coluna "year" uma vez que não é relevante para a análise')
        data = data.drop('year', axis=1)
        st.write(data.head())
    
    # texto para verificar se há valores com straings, valores nulos, e valores duplicados
    with st.expander('**Verificando se há valores com strings, valores nulos e valores duplicados**'):
        st.write('Verificando se há valores com strings')
        st.write(data.applymap(type).eq(str).any())
        st.write('Verificando se há valores nulos')
        st.write(data.isnull().sum())
        st.write('Verificando se há valores duplicados')
        st.write('Dados duplicados: ',data.duplicated().sum())
        st.write('Não há valores com strings, nem valores nulos. Mas há valores duplicados.')
    
    # removendo valores duplicados
    with st.expander('Removendo valores duplicados'):
        data = data.drop_duplicates()
    
    # plotando gráfico de correlação
    with st.expander('**Gráfico de correlação**'):
        st.write('Gráfico de correlação entre os atributos')
        fig, ax = plt.subplots()
        cax = ax.matshow(data.corr(), cmap='coolwarm')  # Use a colormap to better visualize the correlation values
        fig.colorbar(cax)  # Add a colorbar to the figure
        ax.set_yticklabels(data.columns)
        ax.set_xticklabels(data.columns)
        st.pyplot(fig)  

    # visualizando dados utilizando PCA com 3 dimensões e plotando com matplotlib
    with st.expander('**Visualizando dados utilizando PCA com 3 dimensões**'):
        pca = PCA(n_components=3)
        data_pca = pca.fit_transform(data)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data_pca[:, 0], data_pca[:, 1], data_pca[:, 2])
        st.pyplot(fig)
    
    # verificando a distribuição dos dados utilizando matplotlib
    with st.expander('**Distribuição dos dados**'):
        # Deterinar o número de colunas e linhas para os subplots
        divisor = 4
        num_vars = len(data.columns)
        fig, ax = plt.subplots(num_vars // divisor + 1, divisor, figsize=(15, 15))
        for i, var in enumerate(data.columns):
            ax[i // divisor, i % divisor].hist(data[var])
            ax[i // divisor, i % divisor].set_title(var)
        st.pyplot(fig)
    
    # verificando se há outliers
    with st.expander('**Verificando se há outliers**'):
        fig, ax = plt.subplots(num_vars // divisor + 1, divisor, figsize=(15, 15))
        for i, var in enumerate(data.columns):
            ax[i // divisor, i % divisor].boxplot(data[var])
            ax[i // divisor, i % divisor].set_title(var)
        st.pyplot(fig)
    
    # Conclusão do que eu fiz nos dados para poder trabalhar com eles
    st.write('**Resumo das operações realizadas**')
    st.write('1. Drop da coluna "year"')
    st.write('2. Verificação de valores com strings, valores nulos e valores duplicados')
    st.write('3. Remoção de valores duplicados')
    st.write('4. Visualização dos dados utilizando PCA com 3 dimensões')
    st.write('5. Verificação da distribuição dos dados')
    st.write('6. Verificação da presença de outliers')

    # Texto de conclusão
    st.write('**Conclusão**')
    st.write('Os dados foram tratados e estão prontos para serem utilizados em análises futuras')

    # Adicionando botão para download do arquivo
    st.markdown('**Download do arquivo tratado:**')
    st.markdown('Clique no link abaixo para fazer o download do arquivo tratado')
    st.markdown('**[Download do arquivo CSV](https://drive.google.com/file/d/1omUv0zzIfWLgLfK63duBbCeFMCbEfHui/view?usp=drive_link)**')






if __name__ == '__main__':
    main()