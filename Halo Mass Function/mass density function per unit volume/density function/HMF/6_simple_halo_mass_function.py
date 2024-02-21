import numpy as np 
import matplotlib.pyplot as plt 
fig= plt.figure(figsize=(10,8),dpi=100)
from hmf import MassFunction

h= 0.6736
mf= MassFunction()
mf.update(z=8, cosmo_params= {'Om0': 0.315192, 'Ob0': 0.02237/h**2, 'H0':67.36, 'Tcmb0':2.7255, 'Neff': 3.04}, hmf_model='Behroozi')

plt.loglog()
plt.plot(mf.m, mf.dndm, lw= 0.9)
plt.grid()
plt.show()