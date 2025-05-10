""" #genxcode - LEVEL : Spotify Analysis with Streamlit """


# Creation of the interactive website

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu


# Data importation

df = pd.read_csv('../data/spotify.csv')


# Store the initial value of widgets in session state

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False  
    

# Menu


with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options = ["Home", "Visualization"],
        icons = ["house-door", "bar-chart"],
        menu_icon="menu-button-wide",
        default_index=0
        )


# Home Page
    
if selected == "Home":
    
    
    st.title(f"Welcome to the {selected} Page")
    st.text("")
        
    container = st.container(border=True)
       
    container.title('Spotify Vizualization')
    container.markdown('This website will show you  the data of Spotify.')
      
    st.text("")

    st.text("This is my first project on Streamlit.")

    
    
# Visualization Page

if selected == "Visualization":
    
    
    st.title(f"Welcome to the {selected} Page")


# Select Box


    st.title('Popularity of types of music in Spotify')
     
    option = st.selectbox('What kind of chart ?', 
                          ("Bar Chart", 
                           "Scatter Chart"),
                          index=None,
                          placeholder= "Select a visualization method...",
                          label_visibility=st.session_state.visibility)

                
# Group by genre and calculate average popularity              
             
# Bar Chart


    if option == "Bar Chart":
        
        st.write(option, "visualization")
        
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
        
        
    elif option == "Scatter Chart":
        
        st.write(option, "visualization")
        
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
        
        st.info("Please select a visualization method above.")









































