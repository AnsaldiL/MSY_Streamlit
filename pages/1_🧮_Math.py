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
            Le modèle de Schaefer décrit une croissance logistique de la population de Merlu. 
            Ceci implique  un lien linéaire entre l'effort de pêche et le nombre de capture.
            Quant à lui, le modèle de Fox décrit une croissance de Gompertz de la population (Fox, 1970). Cette croissance est plus lente 
            au début et à la fin de la période de simulation. Elle a aussi pour conséquence la relation exponentielle 
            entre le nombre de capture et l'effort de pêche (Fox 1970).   
            """)

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

st.markdown("""
            Ces deux modèles décrivent des types de croissance différentes qui peuvent dépendre de la population étudiée.
            Notons que Punt, A. E. (1992) a montré que le modèle de Fox est en moyenne plus fiable que le modèle de Schaefer pour décrire les
            dynamiques halieutiques. Seulement, ce résultat dépend des populations étudiées. Dans certains cas, le modèle de Schaefer présente de meilleurs résultats
            et inversemnt. Dans un premier temps, Il est donc important de comprendre la manière dont les paramètres r et K influencent les prédictions des modèles. 
            Cette première approche devrait permettre un choix de modèle plus adapté à chaque situation.
            """)