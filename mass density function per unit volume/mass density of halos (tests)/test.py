"""importing necessary modules"""
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
fig=plt.figure(figsize=(10,8),dpi=100)

def mass_density_fun(file_path, box_size):
    """function for plotting mass density per unit volume per unit mass"""
    data =pd.read_csv('file_path')
    x = ['X'].tolsit()
    y = ['Y'].tolsit()
    z = ['Z'].tolsit()
    n = ['N'].tolsit() #number of halos
    m = n* 
    
    frequency, bin_edge = np.histogram(m,bins=b)    
    mass_pt = []
    bin_width = []
    for k in range(len(bin_edge)-1):
        mid_pt = (bin_edge[k+1]+bin_edge[k])/2
        bin_w = (bin_edge[k+1]-bin_edge[k])
        mass_pt.append(mid_pt)
        bin_width.append(bin_w)
    density_fun =[]
    for q in range(len(mass_pt)):
        density_fun.append(frequency[q]/bin_width[q]*(box_size**3))
    #print(bin_edge)
    logx = np.log10(mass_pt)
    logy = np.log10(density_fun)
    #print(np.average(logy))
    plt.plot(logx,logy)
    plt.ylim((0, max(logy)*2))
    plt.title('Mass vs Density Function (log10)')
    plt.xlabel('log( Mass )')
    plt.ylabel('log( Density Function)')
    plt.axhline(y=np.average(logy),linestyle='--',color='red', alpha=0.5)
    plt.text(0,np.average(logy),f'{np.average(logy)}',color='red')
    plt.grid()
    plt.show()

l = 10 # side length
box_size =500.00 # volume = box_size**3
n = 100000 # number of particles
b= 20 #no of bins

mass_density_fun(l,n,b)
