import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8),dpi=100)
import numpy as np

from halomod import TracerHaloModel
import halomod
import hmf

def radial_density_prof():
    z=2
    h=0.71
    Ob0 = 0.02258/h**2
    Ocdm0 = 0.220
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0
    n_s = 0.963
    sigma_8 = 0.8

    #fitting params
    m= -0.10
    A2= 3.44
    b= 430.49
    c0= 3.19
    particle_mass = 2109081520.453063

    #rad density equation paramters
    delta = 200
    G = 4.301*10**-9 #gravitational const (km2 Mpc MSun-1 s)

    hm = TracerHaloModel(z = 2.0,
        hmf_model = 'Behroozi',
        cosmo_params = {
            'Om0': Om0,
            'H0': 70.0,
            'Ob0':Ob0,
            'Tcmb0':2.7255,
            'Neff': 3.04,
        })

    r = np.logspace(-3, 1, 20)
    for m in [1e10, 1e12, 1e16]:
        plt.plot(r, hm.halo_profile.rho(r=r, m=m), label=f'm={m:1.2e}')

radial_density_prof()
plt.legend()
plt.yscale('log')
plt.xscale('log')

plt.xlabel("Distance from Centre [Mpc/h]")
plt.ylabel(r"Halo Density [$h^2 M_\odot {\rm Mpc}^{-3}$]")
plt.grid()
plt.show()