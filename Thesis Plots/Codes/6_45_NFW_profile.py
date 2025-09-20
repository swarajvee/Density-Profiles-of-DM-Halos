import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(7.5,6),dpi=1000)
from matplotlib.ticker import ScalarFormatter
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions
from halomod.halo_model import DMHaloModel



def radial_density_prof_halomod(radius,z,avg_mass):
    h=0.6736
    Ob0 = 0.02237/h**2
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952
    SOdensityL1 = 208.4022045135498

    hm=DMHaloModel(cosmo_model=Planck18,cosmo_params={'Om0':Om0, 'H0':h*100, 'Ob0':Ob0},n=n_s,sigma_8=sigma_8 , z=z,
               mdef_model=mass_definitions.SOMean,mdef_params={'overdensity':SOdensityL1},halo_profile_model='NFWInf',halo_concentration_model='Ludlow16')
    
    r = np.logspace(np.log10(np.min(radius)-0.00001), np.log10(np.max(radius)+0.001), 1000)
    indices = np.argsort(r)

    for i in range(len(avg_mass)):
        rad_density_halomod = hm.halo_profile.rho(r=r[indices], m=avg_mass[i])
        plt.loglog()
        plt.plot(r[indices], rad_density_halomod,'--', lw=0.8, label=f'Mass: {avg_mass[i]:.2e} $M_\odot / h$')


z=0.8
n =100000

radius=[]
for i in range(n):
    rad = np.random.uniform(10**-3,10**3)
    radius.append(rad)

avg_mass = [10**14, 10**15, 10**16, 10**17]

radial_density_prof_halomod(radius,z,avg_mass)

plt.legend()
plt.gca().xaxis.set_major_formatter(ScalarFormatter())
plt.gca().yaxis.set_major_formatter(ScalarFormatter())
plt.title('NFW profile')
plt.xlabel('Radius $Mpc h^{-1}$')
plt.ylabel(r'Radial Density, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$')
plt.grid()
plt.savefig('NFW profile.png')
plt.show()
