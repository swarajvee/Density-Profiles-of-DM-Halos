import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,8),dpi=100)
from colossus.lss import mass_function
from colossus.cosmology import cosmology

#analytic method
def mass_density_fun(file_path,l,b):
    h = 0.6736
    box_size = l/h
    V= box_size**3

    data = pd.read_csv(file_path)
    #mass
    N = data['N'].tolist()
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
    error=[]
    for t in range(len(mass_pt)):
        error.append(np.sqrt(frequency[t])/(bin_width[t]*V))
    plt.loglog()
    plt.scatter(mass_pt,density_fun,label='Observed Mass Density',s=7)
    plt.errorbar(mass_pt,density_fun,yerr=error, fmt='.',capsize=3, label='Error', color= 'gray', alpha= 0.4)
    plt.xlim(10**10.8,10**12.4) 
    return density_fun
    
    
#from colossus
def MassFunc(z,M,l,Om0,Ob0,H0,sigma8,ns,Tcmb0,Neff):
    params={'flat':True,'Om0':Om0, 'Ob0':Ob0, 'H0':H0, 'sigma8':sigma8, 'ns':ns, 'relspecies':True, 'Tcmb0':Tcmb0, 'Neff': Neff, 'Ode0':0.684808}
    cosmology.setCosmology('My_Cosmo',**params, print_warnings = False)

    #plt.loglog()
    mfunc = mass_function.massFunction(M, z, mdef = '200m', model = 'tinker08', q_out ='dndlnM')
    plt.plot(M, np.log(10)*(mfunc/M),'--', label = 'Mass Density using Colossus Package', alpha=0.2, color='red')
    #help(mass_function.massFunction)
    plt.plot(M, density_fun/np.log(10)*(mfunc/M))


#for analytic method
file_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z8.csv'
l = 500 # box size
b= 10 #no of bins
density_fun=mass_density_fun(file_path,l,b)

#for colossus 
z = 8.072500247186802 #redshift
M = 10**np.arange(11.0, 12.3, 0.1)

#cosmological parameters
h= 0.6736
Om0= 0.315192
Ob0= 0.02237/h**2
H0= 67.36
sigma8= 0.807952
ns= 0.9649
Tcmb0= 2.7255
Neff= 3.04

Ocdm0= 0.12/h**2

MassFunc(z,M,l,Om0,Ob0,H0,sigma8,ns,Tcmb0,Neff)

plt.title(f'Mass Density vs Mass (Redshift: {z})')
plt.xlabel(r'$\mathrm{M_{\odot}}$')
plt.ylabel(r'$\mathrm{Density\ Function}$')
plt.legend()
plt.grid()
plt.show()