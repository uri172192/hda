import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from vega_datasets import data
import matplotlib.colors as mcolors

st.set_page_config(layout="wide")
st.title('🏐Scorers')
st.header('🎯Goleadores Asobal')
st.subheader('📌Consulta todos los goleadores según **equipo**:')

df = pd.read_excel("DatasetJugadoresAsobal.xlsx")

## Conseguir lista de equipos
Equipos = df['Equipo'].unique()

## Create the select box
selected_team = st.selectbox('Escoge equipo:', Equipos)

## Filter the data
filtered_data = df[df['Equipo'] == selected_team]

## Generate unique colors for each team (combining multiple color scales)
team_colors1 = dict(zip(Equipos[:8], mcolors.TABLEAU_COLORS.values()))
team_colors2 = dict(zip(Equipos[8:16], mcolors.XKCD_COLORS.values()))
team_colors = {**team_colors1, **team_colors2}

## Graph
graph = alt.Chart(filtered_data).encode(
    x='ToG',
    y=alt.Y("Jugador").sort('-x'),
    text='ToG',
    tooltip=['Jugador', 'Equipo', 'ToG', 'ToS', 'To%'],
    color=alt.Color("Equipo", scale=alt.Scale(domain=list(team_colors.keys()), range=list(team_colors.values())))
)
plotfinal = graph.mark_bar() + graph.mark_text(align='left', dx=2)
st.altair_chart(plotfinal, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**ToG** = Total Goles Marcados")
expander.write("**ToS** = Total Lanzamientos Intentados")
expander.write("**To%** = Porcentaje de acierto en el lanzamiento")

st.divider()

st.subheader('📌Consulta todos los goleadores según **posición**:')
## Conseguir lista de posiciones
Pos = df['Posicion'].unique()

## Create the select box (filter)
selected_pos = st.selectbox('Selecciona posición:', Pos)

## Filter the data
filtered_data = df[df['Posicion'] == selected_pos]

## Graph
graph = alt.Chart(filtered_data).encode(
    x='ToG',
    y=alt.Y("Jugador").sort('-x'),
    text='ToG',
    tooltip=['Jugador', 'Posicion', 'Equipo', 'ToG', 'ToS', 'To%'],
    color=alt.Color("Equipo", scale=alt.Scale(domain=list(team_colors.keys()), range=list(team_colors.values())))
)
plotfinalpos = graph.mark_bar() + graph.mark_text(align='left', dx=2)
st.altair_chart(plotfinalpos, use_container_width=True)

st.caption("🔎Fuente: Asobal")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**ToG** = Total Goles Marcados")
expander.write("**ToS** = Total Lanzamientos Intentados")
expander.write("**To%** = Porcentaje de acierto en el lanzamiento")
