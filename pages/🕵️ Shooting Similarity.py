import streamlit as st 
st.set_page_config(layout="wide")
st.title('🕵️Similitud Jugadores')
st.subheader('📌Descubre los jugadores más similares entre si respecto a su eficacia en el lanzamiento en la Liga Asobal.')

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data
#-------------------------------------
df_jugadores = pd.read_excel("DatasetJugadoresAsobal.xlsx")
#-------------------------------------


# Librerías

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import numpy as np

from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings(action="ignore")

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#Cambiar orden posicion metricas object:
df.insert(1,'Jugador', df.pop("Jugador"))
df.insert(2,'Posicion', df.pop("Posicion"))

#Eliminar columnas:
df.drop(columns='Nº', inplace=True)
df.drop(columns='Equipo', inplace=True)
df.drop(columns='Posicion', inplace=True)

X, y = df.iloc[:, 1:len(df.columns)].values, df.iloc[:, 0].values
X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components = len(df.columns)-1)
pca.fit(X_std)
X_pca = pca.transform(X_std)

print("Shape x_PCA: ", X_pca.shape)
expl = pca.explained_variance_ratio_


#--------------

N_COMP = 8
columns = []

for col in range(1, N_COMP+1, 1):
    columns.append("PCA" + str(col))

df_pca_resultado = pd.DataFrame(data=X_pca[:,0:N_COMP], columns=columns, index = y)

df_pca_resultado.head()

corr_matrix = df_pca_resultado.T.corr(method='pearson')

corr_matrix.head()

## Conseguir llista de equips
players = df['Jugador'].unique()
 
## Create the select box
selected_player = st.selectbox('Escoge jugador:', players)

## Filter the data
filtered_data = df[df['Jugador'] == selected_player]

#---------------------------------------------------

def GetSimilarPlayers(selected_player, num_players, corr_matrix):

    SimPlayers = pd.DataFrame(columns = ['Jugador', 'Similar Player', '% Similitud'])

    row = corr_matrix.loc[corr_matrix.index == selected_player].squeeze()

    for i in range(num_players):
        SimPlayers.at[i, 'Jugador'] = selected_player
        SimPlayers.at[i, 'Similar Player'] = row.nlargest(i + 2).sort_values(ascending=True).index[0]
        SimPlayers.at[i, '% Similitud'] = row.nlargest(i + 2).sort_values(ascending=True)[0]

    return SimPlayers

num_players = 5

df_correlatedPlayers = GetSimilarPlayers(selected_player, num_players, corr_matrix)
st.write(df_correlatedPlayers)
st.caption("🔎Fuente: Asobal")
st.caption('🔎Datos correspondientes a la temproada 22-23 de la liga Asobal.')


#------------------------------------------------------------



