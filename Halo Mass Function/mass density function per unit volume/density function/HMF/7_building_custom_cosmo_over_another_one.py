import sys
import numpy as np 
import matplotlib.pyplot as plt 
fig= plt.figure(figsize=(10,8),dpi=100)
from hmf import MassFunction
from astropy.cosmology import FlatLambdaCDM
from hmf.cosmology.cosmo import Cosmology

#help(Cosmology.__init__)
h= 0.6736
cosmo_params= {'Om0': 0.315192, 'Ob0': 0.02237/h**2, 'Tcmb0':2.7255, 'Neff': 3.04}
cosmo_model= FlatLambdaCDM(name='Planck18', H0=67.36,Om0=0.315192)
cosmo= Cosmology(cosmo_model=cosmo_model, cosmo_params=cosmo_params)


h= 0.6736
mf= MassFunction(cosmo_model, cosmo_params)
mf.update(z=8, cosmo_params= {'Om0': 0.315192, 'Ob0': 0.02237/h**2, 'H0':67.36, 'Tcmb0':2.7255, 'Neff': 3.04}, hmf_model='Behroozi')

plt.loglog()
plt.plot(mf.m, mf.dndm, lw= 0.9)
plt.grid()
plt.show()