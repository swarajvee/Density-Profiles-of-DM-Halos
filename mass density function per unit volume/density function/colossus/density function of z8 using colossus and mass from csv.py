from colossus.lss import mass_function
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

from colossus.cosmology import cosmology
cosmology.setCosmology('planck18')
fig =plt.figure(figsize=(10,8),dpi=100)

def MassFunc(z,l,file_path):
    data= pd.read_csv(file_path)
    M = data['N'].tolist()
    M = np.array(M)
    h = 0.6736
    box_size = l/h
    V= box_size**3

    plt.title('Mass Density using Colossus Package (mass from csv file)')
    plt.xlabel(r'$\log_{10} (\mathrm{Mass})$')
    plt.ylabel(r'$\log_{10} (\mathrm{Density Function})$')
    plt.loglog()
    mfunc = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    plt.scatter(M, mfunc/V, label = 'z = 8', alpha=0.4, s=0.7)
    legend = plt.legend()
    legend.legendHandles[0]._sizes = [50]
    '''plt.xticks(np.linspace(10**11,10**13,5))
    plt.yticks(np.linspace(10**-18,10**-14,5))'''
    plt.grid()
    plt.show()

z = 8
#for getting actual value of M
file_path ='/home/swaraj/Documents/s10 MSc Major Projects/mass density function per unit volume/density function/Hubble data/csv data/z8.csv'
l =500

#M = 10**np.arange(11.0, 15.5, 0.1)

MassFunc(z,l,file_path)