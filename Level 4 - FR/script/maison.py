""" #genxcode - LEVEL : Analyse de Spotify avec Streamlit """


# Création du site web interactif

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


# Importation de données

df = pd.read_csv('../data/spotify.csv')


# Stocker la valeur initiale des widgets dans l'état de la session

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False  
    

# Menu


with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options = ["Home", "Visualisation"],
        icons = ["house-door", "bar-chart"],
        menu_icon="menu-button-wide",
        default_index=0
        )


# Page Home
    
if selected == "Home":
    
    st.title(f"Bienvenu à la page {selected}")
    st.text("")
        
    container = st.container(border=True)
       
    container.title('Visualisation Spotify')
    container.markdown('Ce site vous montrera les données de Spotify.')
      
    st.text("")

    st.text("Il s'agit de mon premier projet sur Streamlit.")

    
    
# Page Visualisation

if selected == "Visualisation":
    
    st.title(f"Bienvenu à la page {selected}")


# Select Box


    st.title('Popularité des types de musique sur Spotify')
     
    option = st.selectbox('Quel type de graphique ?', 
                          ("Graphique en barres", 
                           "Graphique en nuage de points"),
                          index=None,
                          placeholder= "Sélectionnez une méthode de visualisation...",
                          label_visibility=st.session_state.visibility)

                
# Group by genre and calculate average popularity              
             
# Bar Chart


    if option == "Graphique en barres":
        
        st.write(option, "visualisation")
        
        genre_popularity = df.groupby('genre')['popularity'].mean().reset_index()
        
        st.bar_chart(
            
            genre_popularity,
            x='genre',
            y='popularity',
            color="genre",
            width=1000,
            height=500,
            use_container_width=False
            
            )

                
# Scatter Chart
        
        
    elif option == "Graphique en nuage de points":
        
        st.write(option, "visualisation")
        
        genre_popularity = df.groupby('genre')['popularity'].mean().reset_index()
        
        st.scatter_chart(
            
            genre_popularity,
            x='genre',
            y='popularity',
            color="genre",
            width=1000,
            height=500,
            use_container_width=False
            
            )
        
    elif option is None:
        
        st.info("Veuillez sélectionner une méthode de visualisation ci-dessus.")



