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

st.line_chart(data=data, x='Year',y="Catches")




import numpy as np

# Number of years of projections
n=100

# Number of trajectories
n_traj = 100


# Parameters for the Schaeffer model
K = 100
C_MSY = 10
r = 4*C_MSY/K
B_MSY = K/2
h_MSY = C_MSY/B_MSY
N0 = 30




B_shaefer = np.zeros(n+1)
B_shaefer[0] = N0
T = np.zeros(n+1)
T[0]=0


r=st.slider("CHoix de valeur de r",0.0,1.0, step=0.1)
K=st.slider("CHoix de valeur de K",50,5000, step=50)



for i in range(n):
    B_shaefer[i+1] = B_shaefer[i] + r * B_shaefer[i] * (1-B_shaefer[i]/K) - h_MSY*B_shaefer[i]
    T[i+1] = T[i]+1
print(B_shaefer)


sequence = list(range(101))
print(sequence)

colonne1 = sequence
colonne2 = B_shaefer


df = pd.DataFrame({'Temps': colonne1, 'Biomasse': colonne2})
print(df)
st.line_chart( data=df,x='Temps',y="Biomasse")
 


















