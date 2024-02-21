import numpy as np 
import matplotlib.pyplot as plt 
import os
fig=plt.figure(figsize=(10,8),dpi=100)

def mass_density_fun(l,n,b):
    """Mass density function"""
    coordinates = []
    for i in range(n):
        x = np.random.uniform(l,size=None)
        y = np.random.uniform(l,size=None)
        z = np.random.uniform(l,size=None)
        m = np.random.uniform(l,size=None)
        coordinates.append((x,y,z,m))
    x,y,z,m = zip(*coordinates) 
    frequency, bin_edge = np.histogram(m,bins=b)    
    bin_width = []
    for k in range(len(bin_edge)-1):
        mid_pt = (bin_edge[k+1]-bin_edge[k])
        bin_width.append(mid_pt)
    density_fun =[]
    for q in range(len(bin_width)):
        density_fun.append(frequency[q]/(bin_width[q]*(l**3)))
    #print(bin_edge)
    
    plt.plot(density_fun,frequency)
    plt.ylim((0, max(frequency)*2))
    plt.title('Mass vs Density Function')
    plt.xlabel('Mass in Bins')
    plt.ylabel('Density Function')
    plt.axhline(y=np.average(frequency),linestyle='--',color='green')
    plt.text(0,np.average(frequency),f'{np.average(frequency)}',color='red')
    plt.grid()
    plt.show()

l = 10 # side length
v = l**3 # volume
n = 100000 # number of particles
b = 20 #no of bins

mass_density_fun(l,n,b)
