import sys
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi= 100)
from hmf import MassFunction
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions


def halo_mass_function(z):
    h=0.6736
    mf= MassFunction(hmf_model='Behroozi')
    for i in range (len(z)):
        mf.update(z=i, cosmo_model = Planck18, cosmo_params= {'Om0': 0.315192, 'Ob0': 0.02237/h**2, 'Tcmb0':2.7255, 'Neff': 3.04, 'H0': 67.36},sigma_8= 0.807952, n= 0.9649, mdef_model=mass_definitions.SOVirial)
        plt.loglog()
        plt.plot(mf.m, mf.dndlnm, lw=1, label= z[i])

    plt.title('Halo Mass Function in Different Redshifts Using Behroozi Model')
    plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
    plt.ylabel(r"$dn/dlnm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")
    plt.grid()
    plt.legend(title= 'Redshifts')
    plt.show()

z= [0.1,2,3,5,8]
halo_mass_function(z)