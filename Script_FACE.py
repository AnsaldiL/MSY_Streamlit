# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:17:10 2023

@author: lucia
"""
#conda activate FACE
#streamlit run Script_FACE.py
#(FACE) C:\Users\lucia\OneDrive\Bureau\FACE> cd .\OneDrive\Bureau\FACE\MSY_Streamlit

import streamlit as st
import pandas as pd
import numpy as np


DATE_COLUMN = 'Year/Catches'
DATA_URL = ('https://raw.githubusercontent.com/AnsaldiL/MSY_Streamlit/main/data_BiomProd.txt')

def load_data(nrows):
    data = pd.read_fwf(DATA_URL)

    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.caption("Données de captures de merlus en Namibie, entre 1964 et 1999")
st.line_chart(data=data, x='Year',y="Catches")




# Number of years of projections
n= 100 #len(data)


# Parameters for the Schaeffer model


rs= 0.4 #st.slider("Choix de valeur de r",0.0,1.0, step=0.1)
Ks= 1000 #st.slider("Choix de valeur de K",50,5000, step=50)


B_shaefer = np.zeros(n+1)
B_shaefer[0] = Ks/2
T = np.zeros(n+1)
T[0]=0



B_MSY = Ks/2
#h_MSY = C_MSY/B_MSY


h=st.slider("Choix de la pression de pêche", 0.0, 1.0, step=0.1)


#Biomasse avec Schaefer :
for i in range(n):
    B_shaefer[i+1] = B_shaefer[i] + rs * B_shaefer[i] * (1-B_shaefer[i]/Ks) - h*B_shaefer[i]
print(B_shaefer)

sequence = list(range(n+1))
print(sequence)

colonne1 = sequence
biom_schaefer = B_shaefer

df = pd.DataFrame({'Temps': colonne1, 'Biomasse': B_shaefer})
print(df)

st.caption("L'équations de biomasse avec le modèle de Schaefer")
st.latex(r'''
    B_{t+1} = B_t + r.B_t.\left(1 - \frac{B_t}{K} - h.B_t\right)
    ''')
    
st.caption("L'équations de biomasse avec le modèle de Fox")
st.latex(r'''
    B_{t+1} = B_t + r.B_t.\left(1 - \frac{\log(B_t)}{\log(K)} - h.B_t\right)
    ''')
    
st.caption("Evolution de la biomasse en fonction du temps")
st.line_chart( data=df,x='Temps',y="Biomasse")
 












