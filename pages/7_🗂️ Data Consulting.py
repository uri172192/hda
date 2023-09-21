import streamlit as st
import pandas as pd

# Configura el título de la página i favicon
st.set_page_config(page_title="Data Consulting", page_icon="folder.png", layout="wide")
st.title("🗂️Data Consulting")

st.subheader('📌Players Data')
st.write('Consulta datos jugadores Asobal:')
## Df Load
df = pd.read_excel("DatasetJugadoresAsobal.xlsx")
df1 = pd.read_excel("DataJugadoresAsobal2324.xlsx")

# Obtener una lista de temporadas únicas de ambos DataFrames
temporadas = pd.concat([df1['Temporada'], df['Temporada']]).unique()

# Crear el select box para la temporada
selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox1")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data1 = pd.concat([df[df['Temporada'] == selected_temporada1], df1[df1['Temporada'] == selected_temporada1]])

# Obtener una lista de equipos únicos para la temporada seleccionada
equipos_temporada = filtered_data1['Equipo'].unique()

# Crear el select box para el equipo
selected_equipo = st.selectbox('Escoge un equipo:', equipos_temporada)

# Filtrar los datos nuevamente para mostrar solo el equipo seleccionado
filtered_data11 = filtered_data1[filtered_data1['Equipo'] == selected_equipo]

 
## Display the filtered data
st.write(filtered_data11)

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
st.write('Consulta datos equipos Asobal:')
dfteams = pd.read_excel("DatasetEquiposAsobal.xlsx")
dfteams1 = pd.read_excel("DatasetEquiposAsobal2324.xlsx")

# Obtener una lista de temporadas únicas de ambos DataFrames
temporadas = pd.concat([dfteams1['Temporada'], dfteams['Temporada']]).unique()

# Crear el select box para la temporada
selected_temporada1 = st.selectbox('Escoge una temporada:', temporadas, key="selectbox2")

# Filtrar los datos según la temporada seleccionada desde ambos DataFrames
filtered_data1 = dfteams[dfteams['Temporada'] == selected_temporada1], (dfteams1[dfteams1['Temporada'] == selected_temporada1])
 

def round_table_values(df):
    # Aplica redondeo a 2 decimales para todas las celdas del DataFrame
    rounded_df = df.round(2)
    return rounded_df
df_rounded = round_table_values(filtered_data1)
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

