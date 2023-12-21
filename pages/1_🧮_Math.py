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
            
            
            
st.markdown("""
            These mathematical models estimate, based on intrinsic parameter (r,K) for the species studied and the fishing pressure (h),
            the total biomass of this species. These global biomass models are widely used to assess the impact of management measures and
            the state of a stock. We can therefore model biomass at a given time t but also calculate the MSY.
            """)
            
st.subheader("What is this famous MSY ? 🤔")

colabis, colbbis = st.columns(2)
with colabis:
    st.markdown("""
            MSY is a central value for fisheries management. MSY is the maximum quantity of a fish stock that can theoretically
            be harvested without damaging its reproductive capacity, and therefore his durability. When a fish stock is exploided 
            at MSY level, the fishing effort deployed allows optimum catches while limiting the impact on the resource exploited (Ifremer).
            If the stock is exploited above MSY, it will be overfished and catches will fall until the stock collapses.

            """)
        
with colbbis:
    st.image("MSY.jpg")