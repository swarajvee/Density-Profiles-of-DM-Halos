import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi=100)
import os 
import glob

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

halo_min = 100000
halo_max = 101000
file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z0.8/'

def halo_info(halo_min,halo_max,file_dir):
    so_central_X = []
    so_central_Y = []
    so_central_Z = []
    x_L2com_X = []
    x_L2com_Y = []
    x_L2com_Z = []
    particle_number = []
    so_radius = []


    file_paths = glob.glob(os.path.join(file_dir,'halo_info','*halo_info_*.csv'))
    for file_path in file_paths:
        halos = pd.read_csv(file_path)
        N = halos['N']
        indices =[]
        for Ni in N:
            if halo_min <= Ni <= halo_max:
                index = N[N==Ni].index.to_list()
                indices.extend(index)
        for indx in indices:
            so_central_X.append(halos['SO_central_particle_X'][indx])
            so_central_Y.append(halos['SO_central_particle_Y'][indx])
            so_central_Z.append(halos['SO_central_particle_Z'][indx])
            x_L2com_X.append(halos['x_L2com_X'][indx])
            x_L2com_Y.append(halos['x_L2com_Y'][indx])
            x_L2com_Z.append(halos['x_L2com_Z'][indx])
            particle_number.append(halos['N'][indx])
            so_radius.append(halos['SO_radius'][indx])
    return so_central_X,so_central_Y,so_central_Z,x_L2com_X,x_L2com_Y,x_L2com_Z,particle_number,so_radius 

def subsample_data(halo_min,halo_max,file_dir):
    particle_range = f'{halo_min}-{halo_max}'
    X=[]
    Y=[]
    Z=[]
    N=[]
    file_paths = glob.glob(os.path.join(file_dir,'**','**',f'*{particle_range}*','*halo_info_*.csv'))
    for file_path in file_paths:
        subsamples=pd.read_csv(file_path)

        Subsample_A_X = subsamples['Subsample_A_X']
        Subsample_A_Y = subsamples['Subsample_A_Y']
        Subsample_A_Z = subsamples['Subsample_A_Z']
        
        Subsample_B_X = subsamples['Subsample_B_X']
        Subsample_B_Y = subsamples['Subsample_B_Y']
        Subsample_B_Z = subsamples['Subsample_B_Z']
        
        Subsample_X = np.vstack((Subsample_A_X,Subsample_B_X))
        Subsample_Y = np.vstack((Subsample_A_Y,Subsample_B_Y))
        Subsample_Z = np.vstack((Subsample_A_Z,Subsample_B_Z))

        X.extend([number for array in Subsample_X for number in array if not np.isnan(number)])
        Y.extend([number for array in Subsample_Y for number in array if not np.isnan(number)])
        Z.extend([number for array in Subsample_Z for number in array if not np.isnan(number)])
    return X,Y,Z

def radius(x_cent,y_cent,z_cent, x_sub,y_sub,z_sub):
    ra=[]
    for i in range(len(x_cent)):
        for j in range(len(x_sub)):
            rad = np.sqrt((x_sub[j]-x_cent[i])**2+(y_sub[j]-y_cent[i])**2+(z_sub[j]-z_cent[i])**2)
            ra.append(rad)
    print(len(ra))
    return ra

def rad_density_function(radius, particle_mass, b, fraction,z, part_numb):
    bineq = np.logspace(np.min(np.log10(radius)),np.max(np.log10(radius)),b)
    frequency, bin_edge = np.histogram(radius, bins=bineq)

    bin_mass = []
    for i in range(len(frequency)):
        avg_mass = (frequency[i]*particle_mass)/np.sum(part_numb)
        bin_mass.append(avg_mass)
    rad_density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = ((bin_mass[k])/((4/3)*np.pi*((bin_edge[k])**3-(bin_edge[k-1])**3)))*fraction
        mid_pt = (bin_edge[k+1]*bin_edge[k])**(1/2)
        rad_density.append(den)
        mass_pt.append(mid_pt)
    rad_density_comoving = ((1+z)**3)* np.array(rad_density)
    plt.loglog()
    plt.scatter (mass_pt,rad_density_comoving)

def radial_density_prof(part_numb,radius,so_radius,z):

    #cosmo params
    
    h=0.6736
    Ob0 = 0.02237/h**2
    '''Ocdm0 = 0.220
    Onu0 = 0.0
    Om0 = Ocdm0 + Ob0 + Onu0'''
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952
    Ode0=0.684808

    #fitting params
    m= -0.10
    A2= 3.44
    b= 430.49
    c0= 3.19
    particle_mass = 2109081520.453063

    #rad density equation paramters
    delta = SOdensityL1
    G = 4.301*10**(-9) #gravitational const (km2 Mpc MSun-1 s)

    dark_matter_model = halo_model.DMHaloModel(z=z, cosmo_model = Planck18, cosmo_params= {'Om0':Om0, 'Ob0':Ob0 , 'Tcmb0':2.7255, 'Neff': 3.04, 'H0': h*100},sigma_8= sigma_8, n= n_s,mdef_model=mass_definitions.SOMean,halo_concentration_model='Ludlow16',growth_model=GrowthFactor)
    non_linear_mass = dark_matter_model.mass_nonlinear
    
    m200=[]
    for i in range(len(part_numb)):
        M_200 = particle_mass*part_numb[i]
        m200.append(M_200)

    m200_avg = np.sum(m200)/len(part_numb)
    c_delta= A2*((((m200_avg/non_linear_mass)/b)**m)*(1.0+((m200_avg/non_linear_mass)/b)**(-m))-1.0)+c0
    Om = (Om0*(1.0+z)**3.0)
    #H_z = h*100*np.sqrt(Om+(1.0-Om0))
    H_z=h*100*np.sqrt((Om0*(1+z)**3)+Ode0)

    rho_c1 = (3.0*H_z**2.0)/(8.0*3.14*G)
    rho_c = rho_c1/h**2
    rho_m = Om*rho_c
    A1 = np.log(1.0+c_delta)-(c_delta/(1.0+c_delta))
    
    r = radius
    r_delta = max(so_radius)
    #rho = (delta*rho_c)/(3*A1*(r/r_delta)*((1/c_delta)+(r/r_delta))**2)
    rho = (delta*rho_m)/(3*A1*(r/r_delta)*((1/c_delta)+(r/r_delta))**2)
    #rad_density.extend(rho)
    plt.loglog()
    indices = np.argsort(radius)
    sorted_radius = np.array(radius)[indices]
    sorted_rho = np.array(rho)[indices]
    #print(len(rho))
    plt.plot(sorted_radius, sorted_rho,'--',lw=0.8,color='green',label='Equation')

b = 10
particle_mass = 2109081520.453063
fraction = 10
z=0.8
SOdensityL1 = 208.4022045135498

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, particle_number,so_radius = halo_info(halo_min,halo_max,file_dir)
X, Y, Z = subsample_data(halo_min,halo_max,file_dir)
rad = radius(x_L2com_X,x_L2com_Y, x_L2com_Z,X,Y,Z)
rad_density_function(rad, particle_mass, b, fraction,z,particle_number)
radial_density_prof(particle_number,rad,so_radius,z)


plt.show()