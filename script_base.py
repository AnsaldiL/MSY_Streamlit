# Modeling basics populations dynamics with capture

## First model : Shaefer

### Initialisation
import numpy as np
import matplotlib.pyplot as plt
import math as m
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt_py
import matplotlib.lines as mlines

# Number of years of projections
n=100

# Number of trajectories


# Parameters for the Schaeffer model


def K(K):
    return K


def r(r):
    return r

r=0.4
K=100

def C_MSY_Sch(r_value,K_value):
    return (r*K)/4

def B_MSY_Sch(K):
    return K/2

h_MSY_Sch = C_MSY_Sch(r,K)/B_MSY_Sch(K)

def C_MSY_Fox(r,K):
    return (r*K)/(m.exp(1)*log(K)


def B_MSY_Fox(K):
    return (K/m.exp(1))



h_MSY_Fox = C_MSY_Fox(r,K)/B_MSY_Fox(K) 

 
N0 = 30


print(r(10,100))

B_shaefer = np.zeros(n+1)
B_shaefer[0] = N0
T = np.zeros(n+1)
T[0]=0


for i in range(n):
    B_shaefer[i+1] = B_shaefer[i] + r(r) * B_shaefer[i] * (1-B_shaefer[i]/K) - h_MSY(C_MSY,B_MSY)*B_shaefer[i]
    T[i+1] = T[i]+1
print(B_shaefer)

plt.plot(T,B_shaefer)
plt.ylabel('Biomasse')
plt.xlabel('Temps')

## Fox model

B_FOX = np.zeros(n+1)
B_FOX[0] = N0

for i in range(n):
    B_FOX[i+1] = B_FOX[i] + r(C_MSY,K) * B_FOX[i] * (1-m.log(B_FOX[i])/m.log(K)) - h_MSY(C_MSY,B_MSY)*B_FOX[i]
    
plt.plot(T,B_FOX)
plt.ylabel('Biomasse')
plt.xlabel('Temps')
blue_line = mlines.Line2D([], [], color='blue',
                          markersize=15,
                          label='Schaefer')
red_line = mlines.Line2D([], [], color='red',
                          markersize=15,
                          label='Fox')

plt_py.legend(handles=[blue_line,red_line])
plt.show()


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

plt.plot(data['Year'],data['Catches'])
plt.axhline(y=B_MSY(K), color='r', linestyle='-')
plt.axhline(y=C_MSY, color='g', linestyle='-')
red_line = mlines.Line2D([], [], color='r',
                          markersize=15,
                          label='B MSY')
green_line = mlines.Line2D([], [], color='g',
                          markersize=15,
                          label='C MSY')

plt_py.legend(handles=[red_line,green_line])


