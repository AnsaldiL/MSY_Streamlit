# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:24:03 2023

@author: ansal
"""

import streamlit as st
import pandas as pd
import numpy as np
import math as m

st.set_page_config(page_title="Math", page_icon="🧮")
st.write("# Schaefer and Fox model 🧮")



st.subheader("Equations de production de biomasse et de biomasse au MSY avec les modèles de Schaefer et Fox")

cola, colb = st.columns(2)

with cola:
    
    # Equation du modèle de schaefer 
    #st.caption("L'équations de biomasse avec le modèle de Schaefer")
    # st.latex(r'''
    #          B_{t+1} = B_t + r.B_t.\left(1 - \frac{B_t}{K}\right) - h.B_t\\
    #          ''')
    
    
    #st.caption("L'équation du MSY issu du modèle de Schaefer")
    st.latex(r'''
             
             B_{t+1} = B_t + r.B_t.\left(1 - \frac{B_t}{K}\right) - h.B_t\\
             C_{MSY} = \frac{r\times K} {4}
            
             ''')
      
with colb:
         
    # Equation du modèle de FOX   
    #st.caption("L'équations de biomasse avec le modèle de Fox")
    st.latex(r'''
             B_{t+1} = B_t + r.B_t.\left(1 - \frac{\log(B_t)}{\log(K)}\right) - h.B_t\\
             C_{MSY} = \frac{r\times K} {e^1\times \ln{(K)}}
             ''')

    # CMSY with Fox model formalism
    
    #st.caption("L'équation du MSY issu du modèle de Fox")
   