import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi=100)

from halomod import halo_model
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions

from halomod.concentration import Duffy08
from halomod.concentration import GrowthFactor
from halomod.profiles import NFW


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
    plt.scatter(mass_pt, rad_density_comoving,label='Abacus Data')
    plt.xscale('log')
    plt.yscale('log')

def radial_density_prof(part_numb,radius,so_rad_max_index,z):

    #cosmo params
    
    h=0.6736
    Ob0 = 0.02237/h**2
    '''Ocdm0 = 0.220
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0'''
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952

    #fitting params
    m= -0.10
    A2= 3.44
    b= 430.49
    c0= 3.19
    particle_mass = 2109081520.453063

    #rad density equation paramters
    delta = SOdensityL1
    G = 4.303*10**-9 #gravitational const (km2 Mpc MSun-1 s)

    dark_matter_model = halo_model.DMHaloModel(hmf_model='Behroozi' ,z=z, cosmo_model = Planck18, cosmo_params= {'Om0':Om0, 'Ob0':Ob0 , 'Tcmb0':2.7255, 'Neff': 3.04, 'H0': h*100},sigma_8= sigma_8, n= n_s, Mmin=min(np.log10(part_numb)), Mmax= max(np.log10(part_numb)),mdef_model=mass_definitions.SOVirial,halo_concentration_model='Duffy08',growth_model=GrowthFactor)

    non_linear_mass = dark_matter_model.mass_nonlinear
    M200 = particle_mass*particle_number[max_index]

    c_delta= A2*((((M200/non_linear_mass)/b)**m)*(1.0+((M200/non_linear_mass)/b)**(-m))-1.0)+c0
    Om = (Om0*(1.0+z)**3.0)
    H_z = h*100*np.sqrt(Om+(1.0-Om0))
    rho_c = (3.0*H_z**2.0)/(8.0*3.14*G)
    rho_m = Om*rho_c
    A1 = np.log(1.0+c_delta)-(c_delta/(1.0+c_delta))
    
    
    r = radius
    r_delta = so_rad_max_index
    #rho = (delta*rho_c)/(3*A1*(r/r_delta)*((1/c_delta)+(r/r_delta))**2)
    rho = (delta*rho_m)/(3*A1*(r/r_delta)*((1/c_delta)+(r/r_delta))**2)
    
    plt.loglog()
    indices = np.argsort(radius)
    plt.plot(radius[indices], rho[indices],'--',color='green',label='Equation',lw=0.8)

def radial_density_prof_halomod(particle_number, particle_mass, radius,so_radius,z,SOdensityL1):
    '''h=0.71
    Ob0 = 0.02237/h**2 #header value
    Ocdm0 = 0.12
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0
    n_s = 0.9649
    sigma_8 = 0.8'''

    h=0.6736
    Ob0 = 0.02237/h**2
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952

    hm = TracerHaloModel(z = z,
        halo_profile_model = 'NFW',
        cosmo_model = Planck18,
        sigma_8=sigma_8,
        n=n_s,
        mdef_model=mass_definitions.SOMean,
        halo_concentration_model='Ludlow16',
        mdef_params={'overdensity':SOdensityL1},
        cosmo_params = {
            'Om0': Om0,
            'H0': h*100,
            'Ob0':Ob0,
            'Tcmb0':2.7255,
            'Neff': 3.04,
        })
    #print(TracerHaloModel.parameter_info())

    r = np.logspace(np.min(np.log10(radius)), so_radius, 1000)
    m= particle_mass*particle_number
    plt.loglog()
    indices = np.argsort(r)
    plt.plot(r[indices], hm.halo_profile.rho(r=r[indices], m=m))

b = 10
particle_mass = 2109081520.453063
fraction = 10
z=0.8
SOdensityL1 = 208.4022045135498

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, max_index, particle_number,so_radius = halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(x_L2com_X[max_index],x_L2com_Y[max_index], x_L2com_Z[max_index],X,Y,Z)
rad_density_function(rad,so_radius[max_index], particle_mass, b, fraction,z)
radial_density_prof(particle_number,rad,so_radius[max_index],z)
radial_density_prof_halomod(particle_number[max_index], particle_mass, rad,so_radius[max_index],z,SOdensityL1)

plt.grid()
plt.legend()
plt.show()