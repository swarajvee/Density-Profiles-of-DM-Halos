import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(10,8),dpi=100)

print("Reading the data")
def mass_density_fun(file_path,l,b):
    h = 0.6736
    box_size = l/h
    V= box_size**3
    data = pd.read_csv(file_path)
    #mass
    N = data['N'].tolist()

    #coordinates
    x = data['X'].tolist()
    y = data['Y'].tolist()
    z = data['Z'].tolist()

    frequency, bin_edge = np.histogram(N,bins=b)    
    mass_pt = []
    bin_width = []
    for k in range(len(bin_edge)-1):
        mid_pt = (bin_edge[k+1]+bin_edge[k])/2
        bin_w = (bin_edge[k+1]-bin_edge[k])
        mass_pt.append(mid_pt)
        bin_width.append(bin_w)
    density_fun =[]
    for q in range(len(mass_pt)):
        density_fun.append(frequency[q]/(bin_width[q]*(l**3)))
    plt.loglog()
    plt.title('Mass Density vs Mass Graph')
    plt.xlabel(r'$\log_{10} (\mathrm{Mass})$')
    plt.ylabel(r'$\log_{10} (\mathrm{Density Function})$')
    
    plt.scatter(mass_pt,density_fun,label = 'Claculated Mass Density',alpha=0.7)
    
    '''plt.axhline(y=np.average(logy),linestyle='--',color='red', alpha=0.5)
    plt.text(0,np.average(logy),f'{np.average(logy)}',color='red')'''
    plt.legend()
    plt.grid()
    plt.show()

file_path = '/Users/swarajv/Education/s10 MSc Major Project/mass function/mass density function per unit volume/Hubble data/csv data/z8.csv'
l = 500 # box size
b= 100000 #no of bins

mass_density_fun(file_path,l,b)
