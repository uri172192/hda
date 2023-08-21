import streamlit as st
import pandas as pd
import numpy as np
import requests
from PIL import Image
from io import BytesIO

def main():
    # Configurar la página
    st.set_page_config(page_title="HDA", page_icon="playerhda.png", layout="wide")

    # Descargar la imagen desde la URL
    image_url = "https://github.com/uri172192/hda/blob/master/HDA%20SENS%20FONS.png?raw=true"
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Usar CSS personalizado para colocar la imagen encima del menú en la barra lateral
    sidebar_style = """
    <style>
    .sidebar .sidebar-content {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .sidebar .sidebar-content .stImage {
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """

    # Mostrar la imagen en la barra lateral
    st.sidebar.image(image, use_column_width=True)
    
if __name__ == "__main__":
    main()

# Configura el título de la página i favicon
st.title('HDA🤾‍♂️📊')

st.divider()

st.subheader('📌Descripción HDA')
st.write('📢**Handball Data Analytics** se presenta como una aplicación destinada al desarrollo y democratización del análisis de datos en balonmano. La finalidad es ayudar a los usarios a **disfrutar, comprender y compartir los datos sobre el balonmano**.')

st.divider()

st.subheader("📌Contenidos HDA")
st.write("🏐**Scorers**: visualiza los goleadores según equipo y posición")
st.write("🏹**Shooting Distances**: explora los máximos anotadores según la distancia del lanzamiento")
st.write("🎯**Players Shooting Performance**: escoge 2 jugadores y compara su rendimiento en el lanzamiento")
st.write("📋**Efficiency Snapshot Asobal**: conoce como han rendido los equipos durante la temporada")
st.write("🕵️**Shooting Similiraty**: descubre los jugadores similares entre si según su eficacia en el lanzamiento")
st.write("🗂️**Data Consulting**: consulta los datos de los que disponemos sobre cada equipo en materia de lanzamientos")

st.divider()



