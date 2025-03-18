import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

vehicle = []
pos = []
time = []

density = 1/6
length = 300
vmax = 5
psd = 0.01
psd0 = 0.5
iterations = 1000

# Density is avergane number of vhicles per cell
# Length is legnth of road, note road loops round
# vmax is maximum velocity
# psd is the random chance that the vehical slows down 1 cell per tick
# psd0 is probobility vehhicle will not accelrate from rest
# iterations is number of update cycles the system will do

for i in range(0,int(density*length)):
    vehicle.append([i/density,0])
        
nu_vehicle = len(vehicle)

# vehicle stored as list of [x,v] whre x is position and v is current velocity, inital velocity is 0
# nu_vehicle is number of vehicles on simulation

#%%

for k in range(0,iterations):
    
    for i in range(0,nu_vehicle):
        if i != nu_vehicle-1:
            vehicle[i][1] = min(vehicle[i][1] + 1, vmax, vehicle[i+1][0] - vehicle[i][0] - 1)
        else:
                vehicle[i][1] = min(vehicle[i][1] + 1, vmax, (length - 1 - vehicle[i][0]) + vehicle[0][0])
        
# Acceleration and Breaking

    for i in range(0,nu_vehicle):
        if vehicle[i][1] != 0:
            if rng.random() < psd:
                vehicle[i][1] = max(0, vehicle[i][1]-  1)
                
        if vehicle[i][1] == 0:
             if rng.random() < psd0:
                 vehicle[i][1] = 0
        
# Randomisation of velocity, top for v not equal 0, bottom for v = 0

    for i in range(0,nu_vehicle):
        vehicle[i][0] = (vehicle[i][0] + vehicle[i][1])%length
    
# Vehicle postion

    vehicle = sorted(vehicle, key=lambda x:x[0])
    
    for i in range(0,nu_vehicle):
        pos.append(vehicle[i][0])
        time.append(k + 1)
        
# Formates data in such a way it can be plotted
#%%

plt.scatter(time,pos, s=0.01, c='black')

# Polts the data