import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("🗂️Data Consulting")

st.subheader('📌Players Data')
st.write('Consulta datos jugadores Asobal 22/23:')
## Df Load
df_jugadores = pd.read_excel("DatasetJugadoresAsobal.xlsx")

## Get the list of countries
Equipos = df['Equipo'].unique()
 
## Create the select box
selected_team = st.selectbox('Selecciona equipo:', Equipos)
 
## Filter the data
filtered_data = df[df['Equipo'] == selected_team]
 
## Display the filtered data
st.write(filtered_data)

st.caption("🔎Fuente: Asobal")

#Legend
expander = st.expander("➕ **LEGEND**")
expander.write("**Equipo** = Nombre del equipo")
expander.write("**Nº** = Dorsal del jugador")
expander.write("**Posicion** = Posición de juego del jugador")
expander.write("**ToG** = Total Goles Marcados")
expander.write("**ToS** = Total Lanzamientos Intentados")
expander.write("**To%** = Porcentaje total de acierto en el lanzamiento")
expander.write("**L6 (Lanzamientos de 6 metros), L9 (Lanzamientos de 9 metros), L7 (Penaltis), LCO (Lanzamientos de contraataque)** = Siguen el mismo proceso de goles, lanzamientos intentados y porcentaje de acierto según cada distancia o tipo de lanzamiento.")

st.divider()

st.subheader('📌Teams Data')
st.write('Consulta datos equipos Asobal 22/23:')
dfteams = pd.read_excel("DatasetEquiposAsobal.xlsx")
def round_table_values(df):
    # Aplica redondeo a 2 decimales para todas las celdas del DataFrame
    rounded_df = df.round(2)
    return rounded_df
df_rounded = round_table_values(dfteams)
st.write(df_rounded)
st.caption("🔎Fuente: Asobal")

expander = st.expander(" ➕ **LEGEND**")
expander.write("**Equipo** = Nombre del equipo")
expander.write("**PJ** = Partidos Jugados")
expander.write("**GF** = Goles a favor")
expander.write("**GC** = Goles en contra")
expander.write("**Pos** = Número total de posesiones en tota la temporada")
expander.write("**DefRt** = Defensive Rating, eficiencia defensiva")
expander.write("**DefRt** = Defensive Rating, eficiencia defensiva")
expander.write("**OffRt** = Offensive Rating, eficiencia ofensiva")
expander.write("**NetRt** = Net Rating, diferencia entre eficiencia ofensiva y defensiva")
expander.write("**Pace** = ritmo de juego, número de posesiones por partido")
expander.write("**LxGTeam** = Nombre goles anotados por un equipo desde una distancia concreta durante la temproada")
expander.write("**LxSTeam** = Nombre lanzamientos intentados por un equipo desde una distancia concreta durante la temproada")
expander.write("**LxPTeam** = Porcentaje de acierto en el lanzamiento de un equipo desde una distancia concreta durante la temproada")

