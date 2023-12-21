# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:24:03 2023

@author: ansal
"""

import streamlit as st
import pandas as pd
import numpy as np
import math as m

st.set_page_config(page_title="MSY", page_icon="🐠")
st.write("# Why MSY? 🐠")

            
st.subheader("What is this famous MSY? 🤔")


st.markdown("""
            These mathematical models estimate, based on intrinsic parameter ($r$,$K$) for the species studied and the fishing pressure ($h$),
            the total biomass of this species. These global biomass models are widely used to assess the impact of management measures and
            the state of a stock. We can therefore model biomass at a given time t but also calculate the MSY.
            """)
            
            
            
colabis, colbbis = st.columns(2)

            
with colabis:
    st.markdown("""
            MSY is a central value for fisheries management. MSY is the maximum quantity of a fish stock that can theoretically
            be harvested without damaging its reproductive capacity, and therefore his durability. When a fish stock is exploided 
            at MSY level, the fishing effort deployed allows optimum catches while limiting the impact on the resource exploited (Ifremer, 2013).
            If the stock is exploited above MSY, it will be overfished and catches will fall until the stock collapses.
            """)


with colbbis:
    st.image("MSY.jpg")
   
    

st.caption("MSY Schaefer model")
st.latex(r'''             
             C_{MSY} = \frac{r\times K} {4}            
             ''') 
st.caption("MSY Fox model")
st.latex(r'''
             C_{MSY} = \frac{r\times K} {e^1\times \ln{(K)}}
             ''')