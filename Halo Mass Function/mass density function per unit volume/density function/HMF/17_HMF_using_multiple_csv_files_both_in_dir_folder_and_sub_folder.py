import os
import glob
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi= 100)
from hmf import MassFunction
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions
from hmf.mass_function import FittingFunction
import pandas as pd 

def halo_mass_function(z,Mmin,Mmax,model):
    mf= MassFunction(hmf_model=f'{model}',z=z, cosmo_model = Planck18, cosmo_params= {'Om0': 0.315192, 'Ob0': 0.02237/h**2, 'Tcmb0':2.7255, 'Neff': 3.04, 'H0': 67.36},sigma_8= 0.807952, n= 0.9649, mdef_model=mass_definitions.SOVirial, Mmin=np.log10(Mmin),Mmax=np.log10(Mmax))
    #plt.loglog()
    plt.plot(mf.m, mf.dndm,'--', lw=1, label=f'{model}')
    plt.xscale('log')
    plt.yscale('log')

#analytic method
def mass_density_fun(dir_path,l,b):
    box_size = l
    V= box_size**3

    files = glob.glob(os.path.join(dir_path,'**',f'*z{z}*.csv'), recursive=True)
    data_final= []
    for i in range(len(files)):
        data= pd.read_csv(f'{files[i]}')
        data_final.append(data)
    all_data= pd.concat(data_final)
    N = all_data['N'].tolist()

    N = np.array(N)
    bineq = np.logspace(np.log10(min(N)),np.log10(max(N)),b)

    frequency, bin_edge = np.histogram(N,bins=bineq)    
    mass_pt = []
    bin_width = []
    for k in range(len(bin_edge)-1):
        mid_pt = (bin_edge[k+1]*bin_edge[k])**0.5
        bin_w = (bin_edge[k+1]-bin_edge[k])
        mass_pt.append(mid_pt)
        bin_width.append(bin_w)
    density_fun =[]
    for q in range(len(mass_pt)):
        density_fun.append(frequency[q]/(bin_width[q]*V))
    error=[]
    for t in range(len(mass_pt)):
        error.append(np.sqrt(frequency[t])/(bin_width[t]*V))
    plt.loglog()
    plt.scatter(mass_pt,density_fun,label='Observed Mass Density',s=7)
    plt.errorbar(mass_pt,density_fun,yerr=error, fmt='.',capsize=3, label='Error', color= 'gray', alpha= 0.8)
    Mmin, Mmax = min(N)*10**-0.5, max(N)*10**0.5
    return Mmin, Mmax
    
h= 0.6736

z= 0.1
model= 'Behroozi'

#for analytic method
dir_path = f'/Users/swarajv/Education/s10 MSc Major Project/Hubble data/HMFcsvdata'
l = 2000 # box size
b= 10 #no of bins

Mmin, Mmax = mass_density_fun(dir_path, l, b)
halo_mass_function(z,Mmin,Mmax,model)

plt.xlim(Mmin,Mmax)
plt.title(f'Halo Mass Function Comparison in Redshift {z} Using {model} Model')
plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
plt.ylabel(r"$dn/dm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")
plt.grid()
plt.legend()
plt.show()