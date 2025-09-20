import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(dpi=100)

#from halomod import halo_model
#from astropy.cosmology import Planck18
#from hmf.halos import mass_definitions

#from halomod.concentration import Duffy08
#from halomod.concentration import GrowthFactor
#from halomod.profiles import NFW


#import halomod
#import hmf
#from halomod import TracerHaloModel
from astropy.cosmology import Planck18
from hmf.halos import mass_definitions
from halomod.halo_model import DMHaloModel


def halo_info(halo_min,halo_max,file_dir):
    so_central_X = []
    so_central_Y = []
    so_central_Z = []
    x_L2com_X = []
    x_L2com_Y = []
    x_L2com_Z = []
    particle_number = []
    so_radius = []
    r100=[]


    file_paths = glob.glob(os.path.join(file_dir,'halo_info','*halo_info_*.csv'))
    file_paths.sort()
    for file_path in file_paths:
        print("Processing Halo info:", file_path)
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
            r100.append(halos['r100_L2com'][indx])
        del indices
    return so_central_X,so_central_Y,so_central_Z,x_L2com_X,x_L2com_Y,x_L2com_Z,particle_number,so_radius, r100

def subsample_data(halo_min, halo_max, file_dir):
    particle_range = f'{halo_min}-{halo_max}'
    print(particle_range)
    outer_list = []
    
    file_paths = glob.glob(os.path.join(file_dir, '**', '**', f'*{particle_range}*','*halo_info_*.csv'))
    file_paths.sort()
    print("Total file paths:", len(file_paths))
    
    for file_path in file_paths:
        print("Processing file:", file_path)
        subsamples = pd.read_csv(file_path)

        Subsample_A_X = subsamples['Subsample_A_X']
        Subsample_A_Y = subsamples['Subsample_A_Y']
        Subsample_A_Z = subsamples['Subsample_A_Z']
        
        Subsample_B_X = subsamples['Subsample_B_X']
        Subsample_B_Y = subsamples['Subsample_B_Y']
        Subsample_B_Z = subsamples['Subsample_B_Z']
        
        Subsample_X = np.vstack((Subsample_A_X, Subsample_B_X))
        Subsample_Y = np.vstack((Subsample_A_Y, Subsample_B_Y))
        Subsample_Z = np.vstack((Subsample_A_Z, Subsample_B_Z))

        x = [number for array in Subsample_X for number in array if not np.isnan(number)]
        y = [number for array in Subsample_Y for number in array if not np.isnan(number)]
        z = [number for array in Subsample_Z for number in array if not np.isnan(number)]

        outer_list.append((x, y, z))
        
        
    print("Total unique file locations processed:", len(outer_list))
    return outer_list

def radius(x_cent,y_cent,z_cent, subsample_list):
    ra=[]
    for i in range(len(x_cent)):
        rad = np.sqrt(((subsample_list[i][0])-x_cent[i])**2+((subsample_list[i][1])-y_cent[i])**2+(((subsample_list[i][2])-z_cent[i])**2))
        ra.append(rad)
        
    radii=[]
    for j in range(len(ra)):
        radii.append(np.max(ra[j]))
    return radii,ra

def rad_density_function(rad_list, particle_mass, b,z, part_numb):

    min_rad=[]
    max_rad=[]
    for i in range(len(rad_list)):
        min = np.min(rad_list[i])
        max=np.max(rad_list[i])
        min_rad.append(min)
        max_rad.append(max)

    bineq = np.logspace(np.log10(np.min(min_rad)-0.0001),np.log10(np.max(max_rad)+0.01),b)

    freq=0
    for i in range(len(rad_list)):
        frequency, bin_edge = np.histogram(rad_list[i], bins=bineq)
        freq+=frequency
    #upto this everything is okay

    total_mass=0
    for i in range(len(part_numb)):
        total_mass += part_numb[i]*particle_mass
    
    avg_mass=total_mass/len(part_numb)
    fraction= np.sum(part_numb)/np.sum(freq)
    #print(fraction)
    rad_density = []  
    mass_pt = []  
    for k in range(len(bineq)-1):
        den = (avg_mass/((4/3)*np.pi*((bineq[k])**3-(bineq[k-1])**3)))*fraction
        mid_pt = (bineq[k+1]*bineq[k])**(1/2)

        #print(den)

        rad_density.append(den)
        mass_pt.append(mid_pt)
    rad_density_comoving = ((1+z)**3)* np.array(rad_density)
    #print(rad_density_comoving)
    plt.loglog()
    plt.scatter (mass_pt,rad_density_comoving)

def radial_density_prof_halomod(part_numb, part_mass, radius,r100,z,SOdensityL1):
    h=0.6736
    Ob0 = 0.02237/h**2
    Om0 = 0.315192
    n_s = 0.9649
    sigma_8 = 0.807952

    hm=DMHaloModel(cosmo_model=Planck18,cosmo_params={'Om0':Om0, 'H0':h*100, 'Ob0':Ob0},n=n_s,sigma_8=sigma_8 , z=z,
               mdef_model=mass_definitions.SOMean,mdef_params={'overdensity':SOdensityL1},halo_profile_model='NFWInf',halo_concentration_model='Ludlow16')
    #print(TracerHaloModel.parameter_info())

    min_rad=[]
    max_rad=[]
    for i in range(len(radius)):
        min = np.min(radius[i])
        max=np.max(radius[i])
        min_rad.append(min)
        max_rad.append(max)

    r = np.logspace(np.log10(np.min(min_rad)-0.00001), np.log10(np.max(r100)+0.001), 1000)
    indices = np.argsort(r)

    total_mass=0
    for i in range(len(part_numb)):
        total_mass+= part_numb[i]*part_mass
    avg_mass=total_mass/len(part_numb)

    rad_density_halomod = hm.halo_profile.rho(r=r[indices], m=avg_mass)
    print(rad_density_halomod)
    plt.loglog()

    plt.plot(r[indices], rad_density_halomod)


halo_min = 100000
halo_max = 101000
z=0.8
b = 15
particle_mass = 2109081520.453063
SOdensityL1 = 208.4022045135498
file_dir = f'/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z{z}/'

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, particle_number,so_radius, r100 = halo_info(halo_min,halo_max,file_dir)
X_Y_Z_lists = subsample_data(halo_min, halo_max, file_dir)
radi,ra = radius(x_L2com_X, x_L2com_Y, x_L2com_Z, X_Y_Z_lists)
#rad_density_function(ra, particle_mass, b,z,particle_number)
radial_density_prof_halomod(particle_number, particle_mass,ra,r100,z,SOdensityL1)

plt.title('Radial density Profile')
plt.xlabel('Radius $Mpc h^{-1}$')
plt.ylabel(r'Radial Density, $[h^{4}{\rm Mpc}^{-3}M_\odot^{-1}]$')
#plt.savefig('radia_density_profile.png')
plt.show()