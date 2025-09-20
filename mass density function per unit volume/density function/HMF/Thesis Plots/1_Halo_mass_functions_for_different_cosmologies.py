import sys
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(7,5), dpi= 100)
from hmf import MassFunction


def halo_mass_function(z, cosmo_models):
    h=0.6736
    mf= MassFunction(hmf_model='Tinker10')
    for mod in cosmo_models:
        mf = MassFunction(z=z, cosmo_params={'Om0': 0.315192}, hmf_model= mod)
        plt.loglog()
        plt.plot(mf.m, mf.dndlnm, lw=1, label=mod)

    plt.title(f'Halo Mass Function in {z} Redshift Using Different Cosmological Models')
    plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
    plt.ylabel(r"$dn/dlnm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")
    plt.grid()
    plt.legend(title= 'Cosmo Models')
    plt.show()

cosmo_models=['Behroozi','Tinker10','Warren','Tinker08','Jenkins']
z=8
halo_mass_function(z, cosmo_models)