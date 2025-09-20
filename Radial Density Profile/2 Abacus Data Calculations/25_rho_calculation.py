import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,8), dpi=100)

from halomod import halo_model
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions

from halomod.concentration import Duffy08
from halomod.concentration import GrowthFactor
from halomod.profiles import NFW


file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2'
file_name = 'halo_info_000'

def halo_info(file_dir,file_name):
    halo = pd.read_csv(file_dir+'/halo_info/'+file_name+'.csv')
    
    so_central_X = halo['SO_central_particle_X']
    so_central_Y = halo['SO_central_particle_Y']
    so_central_Z = halo['SO_central_particle_Z']

    particle_number =halo['N']
    max_index = np.argmax(particle_number)

    so_radius = halo['SO_radius']
    return so_central_X, so_central_Y, so_central_Z, max_index, so_radius, particle_number

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

def radial_density_prof(part_numb,radius,so_rad_max_index):

    #cosmo params
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

    dark_matter_model = halo_model.DMHaloModel(hmf_model='Behroozi' ,z=z, cosmo_model = Planck18, cosmo_params= {'Om0':Om0, 'Ob0':Ob0 , 'Tcmb0':2.7255, 'Neff': 3.04, 'H0': h*100},sigma_8= sigma_8, n= n_s, Mmin=min(np.log10(part_numb)), Mmax= max(np.log10(part_numb)),mdef_model=mass_definitions.SOVirial,halo_concentration_model='Duffy08',growth_model=GrowthFactor)

    non_linear_mass = dark_matter_model.mass_nonlinear
    M200 = particle_mass*particle_number[max_index]

    c_delta= A2*((((M200/non_linear_mass)/b)**m)*(1+((M200/non_linear_mass)/b)**(-m))-1)+c0
    A1 = np.log(1+c_delta)-c_delta/(1+c_delta)
    rho_c = (3*h*100)/(8*3.14*G)
    r = radius
    r_delta = so_rad_max_index
    rho = (delta*rho_c)/(3*A1*(r/r_delta)*(1/(c_delta+(r/r_delta)))**2)
    return radius,rho





so_central_X, so_central_Y, so_central_Z, max_index, so_radius, particle_number = halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(so_central_X[max_index],so_central_Y[max_index], so_central_Z[max_index],X,Y,Z)
radius, rho = radial_density_prof(particle_number,rad,so_radius[max_index])

plt.loglog()
indices = np.argsort(radius)
plt.plot(radius[indices], rho[indices])
plt.show()