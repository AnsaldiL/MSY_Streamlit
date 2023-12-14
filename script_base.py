# Modeling basics populations dynamics with capture

## First model : Shaefer

### Initialisation
import numpy as np
import matplotlib.pyplot as plt
import math as m

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



for i in range(n):
    B_shaefer[i+1] = B_shaefer[i] + r * B_shaefer[i] * (1-B_shaefer[i]/K) - h_MSY*B_shaefer[i]
    T[i+1] = T[i]+1
print(B_shaefer)

plt.plot(T,B_shaefer)
plt.ylabel('Biomasse')
plt.xlabel('Temps')

## Fox model

B_FOX = np.zeros(n+1)
B_FOX[0] = N0

for i in range(n):
    B_FOX[i+1] = B_FOX[i] + r * B_FOX[i] * (1-m.log(B_FOX[i])/m.log(K)) - h_MSY*B_FOX[i]
    
plt.plot(T,B_FOX)
plt.ylabel('Biomasse')
plt.xlabel('Temps')


