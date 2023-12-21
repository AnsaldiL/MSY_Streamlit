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



st.subheader("Biomass and MSY biomass production equations with Schaefer and Fox models")

cola, colb = st.columns(2)

st.markdown("""
            Schaefer's model describes the logistic growth of the hake population. 
            This implies a linear relationship between fishing effort and catch numbers.
            Fox's model, on the other hand, describes Gompertz population growth (Fox, 1970). This growth is slower 
            at the beginning and end of the simulation period. It also results in the exponential relationship 
            between the number of catches and fishing effort (Fox 1970).  
            """)

with cola:
    
    # Equation du modèle de schaefer 
    #st.caption("L'équations de biomasse avec le modèle de Schaefer")
    # st.latex(r'''
    #          B_{t+1} = B_t + r.B_t.\left(1 - \frac{B_t}{K}\right) - h.B_t\\
    #          ''')
    
    
    st.caption("Modèle de Schaefer")
    st.latex(r'''
             
             B_{t+1} = B_t + r.B_t.\left(1 - \frac{B_t}{K}\right) - h.B_t\\
             C_{MSY} = \frac{r\times K} {4}
            
             ''')
      
with colb:
         
    # Equation du modèle de FOX   
    st.caption("Modèle de Fox")
    st.latex(r'''
             B_{t+1} = B_t + r.B_t.\left(1 - \frac{\log(B_t)}{\log(K)}\right) - h.B_t\\
             C_{MSY} = \frac{r\times K} {e^1\times \ln{(K)}}
             ''')

    # CMSY with Fox model formalism
    
    #st.caption("L'équation du MSY issu du modèle de Fox")

st.markdown("""
            These two models describe different types of growth, which may depend on the population studied.
            Note that Punt, A. E. (1992) has shown that the Fox model is on average more reliable than the Schaefer model for describing
            fishery dynamics. However, this result depends on the populations studied. In some cases, the Schaefer model gives better results
            and vice versa. As a first step, it is therefore important to understand how the parameters r and K influence model predictions. 
            This initial approach should enable us to select the most appropriate model for each situation.
            """)