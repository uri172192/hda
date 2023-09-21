import streamlit as st
import pandas as pd


# Configura el título de la página i favicon
st.set_page_config(page_title="Snapshot Asobal", page_icon="clipboard.png", layout="wide")
st.title("📋Efficiency Snapshot Asobal")
st.subheader('📌Como han rendido los equipos de la liga Asobal durante la temporada 23-24?')

import streamlit as st
import plotly.express as px

# Obtener los datos del dataset iris de Plotly Express
dfteams = pd.read_excel("DatasetEquiposAsobal2324.xlsx")



# Redondear los valores a 2 decimales en las columnas "OffRt" y "DefRt"
dfteams["OffRt"] = dfteams["OffRt"].round(2)
dfteams["DefRt"] = dfteams["DefRt"].round(2)
dfteams["NetRt"] = dfteams["NetRt"].round(2)

fig = px.scatter(dfteams, x="OffRt", y="DefRt", color='Equipo',
                 text='Equipo', log_x=True, hover_data=['NetRt'], color_continuous_scale='plotly')
fig.update_yaxes(autorange="reversed")
fig.update_xaxes(title_text='Rating Ofensivo')
fig.update_yaxes(title_text='Rating Defensivo')
fig.update_traces(marker_size=25)
fig.update_traces(textfont=dict(color='black', size=25, family='Tahoma, bold'), textposition='bottom center')
fig.update_traces(marker=dict(line=dict(color='black', width=3)))
fig.update_layout(width=1200, height=800)
fig.update_layout(xaxis_title_font=dict(size=20), yaxis_title_font=dict(size=20))
fig.update_traces(hoverlabel_font_size=20, hoverlabel_font_family='Tahoma, bold')
fig.update_traces(hovertemplate="<b>%{text}</b><br>OffRt: %{x}<br>DefRt: %{y}<br>NetRt: %{customdata[0]}")
fig.update_traces(hoverlabel_namelength=0)

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

st.caption("🔎Fuente: Asobal")
st.caption("🔎Ratings: Ajustado por 50 posesiones")

st.divider()

st.subheader('📌Teams Data')
st.write('Consulta datos equipos Asobal 23-24:')
## Df Load
dfteams = pd.read_excel("DatasetEquiposAsobal2324.xlsx")
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



