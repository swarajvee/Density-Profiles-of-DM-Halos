import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(10,8),dpi=100)
from colossus.lss import mass_function
from colossus.cosmology import cosmology

#adding a new cosmology

"""  *********  MY COSMOS ************
    om0, omega_M, cosmological parameter= 0.315192
    H0, hubble constant= 67.36
    ob0,omega_b, baryon density= 0.02237
    sigma8, ZD_Pk_norm, power spectrum normalization= 8.0 
    ns, n_s, spectral index of the primordial power spectrum= 0.9649"""





#analytic method
def mass_density_fun(file_path,l,b):
    h = 0.6736
    box_size = l/h
    V= box_size**3

    data = pd.read_csv(file_path)
    #mass
    N = data['N'].tolist()

    #coordinates
    '''x = data['X'].tolist()
    y = data['Y'].tolist()
    z = data['Z'].tolist()'''
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
    #plt.errorbar(mass_pt,density_fun)
    
    
#from colossus
def MassFunc(z,M,l):
    h = 0.6736
    box_size = l/h
    V= box_size**3

    cosmo= cosmology.setCosmology('planck18-only')
    cosmo.H0= 67.36
    cosmo.Om0= 0.315192
    #cosmo.Ob0= 0.02237
    cosmo.sigma8= 0.807952
    cosmo.ns= 0.9649
    #cosmo.flat=  0.1200

    cosmo.checkForChangedCosmology()

    #plt.loglog()
    mfunc = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    plt.plot(M, 2.303*(mfunc/M),'--', label = 'Mass Density using Colossus Package', alpha=0.2, color='red')
    


#for analytic method
file_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z8.csv'
l = 500 # box size
b= 8 #no of bins
mass_density_fun(file_path,l,b)

#for colossus 
z = 8.072500247186802 #redshift
M = 10**np.arange(11.0, 12.3, 0.1)
MassFunc(z,M,l)

plt.title(f'Mass Density vs Mass (Redshift: {z})')
plt.xlabel(r'$\mathrm{M_{\odot}}$')
plt.ylabel(r'$\mathrm{Density\ Function}$')
plt.legend()
plt.grid()
plt.show()