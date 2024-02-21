import numpy as np 
import matplotlib.pyplot as plt 
plt.figure(figsize=(25, 9.5), dpi=100)
from hmf import MassFunction

def halo_mass_function(z):
    models = [
        'Behroozi', 'Tinker10', 'PS', 'SMT', 'ST', 'Jenkins', 'Warren', 'Reed03', 
        'Reed07', 'Peacock', 'Angulo', 'AnguloBound', 'Watson_FoF', 'Watson', 
        'Crocce', 'Courtin', 'Bhattacharya', 'Tinker08', 'Pillepich', 'Manera', 
        'Ishiyama', 'Bocquet200mDMOnly', 'Bocquet200mHydro', 'Bocquet200cDMOnly', 
        'Bocquet200cHydro', 'Bocquet500cDMOnly', 'Bocquet500cHydro'
    ]
    plt.loglog()
    
    for i in models:
        mf = MassFunction(z=z, cosmo_params={'Om0': 0.315192}, hmf_model= i)
        plt.plot(mf.m, mf.dndm, lw=0.5, label=i)
        
z = 10
halo_mass_function(z)

plt.title(f'Halo Mass Function Comparison in Redshift {z} Using Different Models')
plt.xlabel(r"Mass, $[h^{-1}M_\odot]$")
plt.ylabel(r"$dn/dm$, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$")
plt.grid()
plt.legend(title='Cosmological Models')
plt.show()