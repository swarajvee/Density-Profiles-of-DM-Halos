from colossus.lss import mass_function
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

from colossus.cosmology import cosmology
cosmology.setCosmology('planck18')
fig =plt.figure(figsize=(10,8),dpi=100)

def MassFunc(z,M,l):
    h = 0.6736
    box_size = l/h
    V= box_size**3

    plt.title('Mass Density using Colossus Package')
    plt.xlabel(r'$\log_{10} (\mathrm{Mass})$')
    plt.ylabel(r'$\log_{10} (\mathrm{Density Function})$')
    plt.loglog()

    mfunc = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    plt.plot(M, 2.303*(mfunc/M),'--', label = 'z8 with generated mass', alpha=0.4, color='red')

    legend = plt.legend()
    legend.legendHandles[0]._sizes = [50]
    plt.grid()
    plt.show()

z = 8
l =500
M = 10**np.arange(11.0, 12.3, 0.1)

MassFunc(z,M,l)