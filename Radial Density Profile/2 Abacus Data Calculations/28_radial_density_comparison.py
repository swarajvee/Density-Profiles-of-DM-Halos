import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8),dpi=100)
import numpy as np
import pandas as pd

import halomod
import hmf
from halomod import TracerHaloModel
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions

file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z0.8'
file_name = 'halo_info_000'

def halo_info(file_dir,file_name):
    halo = pd.read_csv(file_dir+'/halo_info/'+file_name+'.csv')
    so_central_X = halo['SO_central_particle_X']
    so_central_Y = halo['SO_central_particle_Y']
    so_central_Z = halo['SO_central_particle_Z']

    x_L2com_X = halo['x_L2com_X']
    x_L2com_Y = halo['x_L2com_Y']
    x_L2com_Z = halo['x_L2com_Z']
    
    particle_number =halo['N']
    max_index = np.argmax(particle_number)
    so_radius = halo['SO_radius']
    return so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, max_index, particle_number, so_radius

def subsample(file_dir, file_name):
    subsamples = pd.read_csv(file_dir+'/subsample data/'+file_name+'_subsample_data.csv')

    Subsample_A_X = subsamples['Subsample_A_X']
    Subsample_A_Y = subsamples['Subsample_A_Y']
    Subsample_A_Z = subsamples['Subsample_A_Z']

    Subsample_B_X = subsamples['Subsample_B_X']
    Subsample_B_Y = subsamples['Subsample_B_Y']
    Subsample_B_Z = subsamples['Subsample_B_Z']
    
    Subsample_X = np.vstack((Subsample_A_X,Subsample_B_X))
    Subsample_Y = np.vstack((Subsample_A_Y,Subsample_B_Y))
    Subsample_Z = np.vstack((Subsample_A_Z,Subsample_B_Z))

    X=[]
    Y=[]
    Z=[]
    X.extend([number for array in Subsample_X for number in array if not np.isnan(number)])
    Y.extend([number for array in Subsample_Y for number in array if not np.isnan(number)])
    Z.extend([number for array in Subsample_Z for number in array if not np.isnan(number)])
    return X, Y, Z

def radius(x_cent,y_cent,z_cent, x_sub,y_sub,z_sub):
    rad = np.sqrt((x_sub-x_cent)**2+(y_sub-y_cent)**2+(z_sub-z_cent)**2)
    return rad

def rad_density_function(radius,so_radius_max, particle_mass, b, fraction,z):

    bineq = np.logspace(np.min(np.log10(radius)),np.max(np.log10(so_radius_max)),b)
    frequency, bin_edge = np.histogram(radius, bins=bineq)

    bin_mass = []
    for i in range(len(frequency)):
        mass = frequency[i]*particle_mass
        bin_mass.append(mass)
    rad_density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = ((bin_mass[k])/((4/3)*np.pi*((bin_edge[k])**3-(bin_edge[k-1])**3)))*fraction
        mid_pt = (bin_edge[k+1]*bin_edge[k])**(1/2)
        rad_density.append(den)
        mass_pt.append(mid_pt)
    rad_density_comoving = ((1+z)**3)* np.array(rad_density)
    plt.loglog()
    plt.scatter(mass_pt, rad_density_comoving,label='Abacus Data')
    return rad_density_comoving, mass_pt

def radial_density_prof(particle_number, particle_mass, radius,so_radius,z):
    '''h=0.71
    Ob0 = 0.02237/h**2 #header value
    Ocdm0 = 0.12
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0
    n_s = 0.9649
    sigma_8 = 0.8'''

    h=0.6736  #new value
    Ob0 = 0.02258/h**2
    Ocdm0 = 0.12
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0
    n_s = 0.9649
    sigma_8 = 0.8

    hm = TracerHaloModel(z = z,
        hmf_model = 'Behroozi',
        halo_profile_model = 'NFW',
        cosmo_model = Planck18,
        sigma_8=sigma_8,
        n=n_s,
        halo_concentration_model='Ludlow16',
        mdef_model=mass_definitions.SOVirial,
        cosmo_params = {
            'Om0': Om0,
            'H0': h*100,
            'Ob0':Ob0,
            'Tcmb0':2.7255,
            'Neff': 3.04,
        })

    r = np.logspace(np.min(np.log10(radius)), so_radius, 1000)
    m= particle_mass*particle_number
    plt.loglog()
    indices = np.argsort(r)
    plt.plot(r[indices], hm.halo_profile.rho(r=r[indices], m=m))



b = 10
particle_mass = 2109081520.453063
fraction = 10
z=0.8

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, max_index, particle_number,so_radius = halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(x_L2com_X[max_index],x_L2com_Y[max_index], x_L2com_Z[max_index],X,Y,Z)
rad_density_function(rad,so_radius[max_index], particle_mass, b, fraction,z)
radial_density_prof(particle_number[max_index], particle_mass, rad,so_radius[max_index],z)

#print(particle_number[max_index])
#plt.loglog()
plt.legend()
plt.xlabel("Distance from Centre [Mpc/h]")
plt.ylabel(r"Halo Density [$h^2 M_\odot {\rm Mpc}^{-3}$]")
plt.grid()
plt.show()