import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from colossus.lss import mass_function
from colossus.cosmology import cosmology
cosmology.setCosmology('planck18')

fig=plt.figure(figsize=(10,8),dpi=100)

#analytic method
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
    bineq = np.logspace(np.log10(min(N)),np.log10(max(N)),b)

    frequency, bin_edge = np.histogram(N,bins=bineq)    
    mass_pt = []
    bin_width = []
    for k in range(len(bin_edge)-1):
        mid_pt = (bin_edge[k+1]+bin_edge[k])/2
        bin_w = (bin_edge[k+1]-bin_edge[k])
        mass_pt.append(mid_pt)
        bin_width.append(bin_w)
    density_fun =[]
    for q in range(len(mass_pt)):
        density_fun.append(frequency[q]/(bin_width[q]*V))
    plt.loglog()
    plt.scatter(mass_pt,density_fun,label='Observed Mass Density',s=7)
    
#from colossus
def MassFunc(z,M,l):
    h = 0.6736
    box_size = l/h
    V= box_size**3

    plt.loglog()
    mfunc = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    plt.plot(M, mfunc/(M),'--', label = 'Mass Density using Colossus Package', alpha=0.2, color='red')


#for analytic method
file_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z8.csv'
l = 500 # box size
b= 20 #no of bins
mass_density_fun(file_path,l,b)

#for colossus 
z = 8 #redshift
M = 10**np.arange(11.0, 12.3, 0.1)
MassFunc(z,M,l)

plt.title(f'Mass Density vs Mass (Redshift: {z})')
plt.xlabel(r'$\log_{10} (\mathrm{Mass})$')
plt.ylabel(r'$\log_{10} (\mathrm{Density Function})$')
plt.legend()
plt.grid()
plt.show()