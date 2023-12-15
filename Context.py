# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:54:26 2023

@author: ansal
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Context",
    page_icon="🐟",
)

st.write("# Hake fisheries in Namibia 🐟")

st.sidebar.success("Select a page above")

st.markdown(
    """
    The hake trawl fishery accounts for around half of the landed value of all 
    South African commercial fisheries and is a major contributor to
    Namibia's gross domestic product. In the 60s and 70s, 
    hake stocks were heavily exploited by numerous foreign fleets. 
    This intensification of the fishing effort led to the collapse of 
    stocks (Butterworth and Rademeyer, 2005).
    ### How Schaefer and Fox model could help us to understand overfishing ?
    - Have a look to the mathematical model
    - Learn more about MSY and its importance to set fishing threshold
"""
)

st.subheader('Principal ports of Namibia')

lon = [15.157, 14.51]
lat = [-26.6477778, -22.9]
df_map = pd.DataFrame({'latitude': lat, 'longitude': lon})

st.map(df_map)

st.subheader("References")
st.markdown("""
        Butterworth, D. S. and Rademeyer, R. A. (2005). Sustainable Management 
         Initiatives for the Southern African Hake Fisheries Over Recent Years.
         Bulletin of Marine Science, 76(2) :287–320
         """)