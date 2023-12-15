# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:17:10 2023

@author: lucia
"""

import streamlit as st
import pandas as pd
import numpy as np
import math as m

st.set_page_config(page_title="Model", page_icon="📈")
st.write("# Modelling the fishing dynamic 📈")

DATE_COLUMN = 'time/catches'
DATA_URL = ('https://raw.githubusercontent.com/AnsaldiL/MSY_Streamlit/main/data_BiomProd.txt')

def load_data(nrows):
    data = pd.read_fwf(DATA_URL)

    return data

# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.

data = load_data(10000)

# Notify the reader that the data was successfully loaded.
#data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# Number of years of projections
n= 100 #len(data)



rs = st.slider("Value of **r** *(growth rate)*?",0.0,1.0, step=0.005)
Ks = st.slider("Value of **K** *(carrying capacity)*?",50,5000, step=5)
h=st.slider("Value of **h** *(harvest rate)*?", 0.0, 1.0, step=0.01)

col2, col3 = st.columns(2)


with col2:
    C_MSY_Shaefer = (rs*Ks)/4
    C_MSY_Fox = (rs*Ks)/(m.exp(1)*m.log(Ks))

    data['CMSY Shaefer'] = np.repeat(C_MSY_Shaefer, len(data))
    data['CMSY Fox'] = np.repeat(C_MSY_Fox, len(data))

    st.subheader("Hake catches")
    st.line_chart(data=data, x='Year',y=["Catches","CMSY Shaefer","CMSY Fox"])


with col3:
    
    #Schaefer Model
    
    B_shaefer = np.zeros(n+1)
    B_shaefer[0] = Ks/2
    # TIme initialisation
    T = np.zeros(n+1)
    T[0]=0
    
    for i in range(n):
        B_shaefer[i+1] = B_shaefer[i] + rs * B_shaefer[i] * (1-B_shaefer[i]/Ks) - h*B_shaefer[i]
    print(B_shaefer)
    
    B_FOX = np.zeros(n+1)
    B_FOX[0] = Ks/2

    #Fox Model
    for i in range(n):
        B_FOX[i+1] = B_FOX[i] + rs * B_FOX[i] * (1-m.log(B_FOX[i])/m.log(Ks)) - h*B_FOX[i]
    print(B_FOX)
    
    #Time sequence
    sequence = list(range(n+1))

    colonne1 = sequence
    
    df = pd.DataFrame({'time': colonne1, 'Fox': B_FOX, 'Schaefer': B_shaefer})
    
    st.subheader("Change in biomass over time")
    st.line_chart(data=df,x='time',y=["Schaefer", "Fox"])