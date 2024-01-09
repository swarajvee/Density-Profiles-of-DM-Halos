from colossus.lss import mass_function
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

from colossus.cosmology import cosmology
cosmology.setCosmology('planck18')
fig =plt.figure(figsize=(10,8),dpi=100)

def MassFunc(z,l,file_path,N):
    data= pd.read_csv(file_path)
    M = data['N'].tolist()
    M = np.array(M)
    h = 0.6736
    box_size = l/h
    V= box_size**3

    mfunc1 = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    mfunc2 = mass_function.massFunction(N, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    #print(mfunc1)
    plt.title('Mass Density using Colossus Package')
    plt.xlabel(r'$\log_{10} (\mathrm{Mass})$')
    plt.ylabel(r'$\log_{10} (\mathrm{Density Function})$')
    plt.loglog()

    plt.scatter(M, mfunc1/V, label = 'z8 with csv data', alpha=0.4, s=0.7)
    plt.plot(N, mfunc2/V,'--', label = 'z8 with generated mass', alpha=0.4, color='red')

    legend = plt.legend()
    legend.legendHandles[0]._sizes = [50]
    plt.grid()
    plt.show()

z = 8
#for getting actual value of M
file_path ='/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z8.csv'
l =500
N = 10**np.arange(11.0, 12.3, 0.1)

MassFunc(z,l,file_path,N)
