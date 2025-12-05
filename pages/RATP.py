import streamlit as st
from PIL import Image
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# Section RATP
st.markdown("<h1 class='main-header' style='color:#4bc0ad;' >🖥️ Exercice Python & Streamlit</h1>", unsafe_allow_html=True)

df=pd.read_csv("emplacement-des-gares-idf.csv", sep=";")
st.write ("Aperçu du jeu de données :")
st.write ("Le jeu de données porte sur toutes les stations du réseau IDF Mobilités")
st.write (df.head(10))
st.write("")
st.write("")
st.write("")

counts = df['idf'].value_counts()

# Création du camembert
fig = px.pie(
    values=counts.values,
    names=["Île-de-France", "Hors Île-de-France"],
    color=["Île-de-France", "Hors Île-de-France"],  # pour gérer les couleurs
    color_discrete_map={
        "Île-de-France": "#4bc0ad",      
        "Hors Île-de-France": "#ffffff"   
    }
)

# Options de mise en forme
fig.update_traces(
    textinfo='label+percent',
    textfont_size=12  # taille du texte
)

fig.update_layout(
    width=300,   # largeur du graphique
    height=400,  # hauteur du graphique
    margin=dict(t=20, b=20, l=20, r=20)
)

st.plotly_chart(fig)

stations_par_ligne = df['indice_lig'].value_counts().sort_index()
fig = px.bar(
            x=stations_par_ligne.index,
            y=stations_par_ligne.values,
            labels={"x": "ligne de metro", "y": "Nombre de stations sur la ligne"},
            title="Stations par ligne de métro",
            color=stations_par_ligne.values,
            color_discrete_sequence=["#004fa3"]
        )

# Affichage dans Streamlit
st.plotly_chart(fig)

st.markdown("""
<style>
.img-small img {
    width: 50px;      
    height: auto;     
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="img-small">', unsafe_allow_html=True)
st.image("RATP.png")
st.markdown("</div>", unsafe_allow_html=True)

