import numpy as np 
import matplotlib.pyplot as plt 
fig= plt.figure(figsize=(10,8),dpi=100)
from hmf import MassFunction

#MassFunction.parameter_info(['cosmso_model','sigma_8'])

mf= MassFunction()
#mf.quantities_available()

plt.loglog()
plt.plot(mf.m, mf.dndm,lw=1)
plt.grid()
plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
plt.ylabel(r"$dn/dm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")
plt.show()