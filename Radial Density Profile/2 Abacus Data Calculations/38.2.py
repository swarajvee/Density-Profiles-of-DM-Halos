import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def subsample_data(halo_min, halo_max, file_dir):
    particle_range = f'{halo_min}-{halo_max}'
    outer_list = []
    
    file_paths = glob.glob(os.path.join(file_dir, '**', '**', f'*{particle_range}*','*halo_info_*.csv'))
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
        rad = np.sqrt((subsample_list[i][0]-x_cent[i])**2+(subsample_list[i][1]-y_cent[i])**2+(subsample_list[i][2]-z_cent[i])**2)
        ra.append(rad)
    return ra

def rad_density_function(radius, particle_mass, b, fraction,z, part_numb):

    frequency=0
    binedge=0
    for i in range(len(radius)):
        bineq = np.logspace(np.min(np.log10(radius[i]+0.0001)),np.max(np.log10(radius[i]+0.0001)),b)
        freq, bin_edge = np.histogram(radius[i], bins=bineq)
        frequency +=freq
        binedge+=bin_edge
        #print(bin_edge)
    edge = binedge/len(radius)

    #bin_mass = []
    '''P_total=0
    for j in range(len(frequency)):
        P_total += frequency[j]

    avg_mass=(P_total*particle_mass)/len(radius)

    print(len(frequency))
    print(P_total)'''

    total_mass=0
    for i in range(len(part_numb)):
        total_mass+=np.sum(part_numb)

    avg_mass=total_mass*particle_mass/len(part_numb)
    print(avg_mass)

    rad_density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = ((avg_mass)/((4/3)*np.pi*((edge[k])**3-(edge[k-1])**3)))*fraction
        #den = ((avg_mass)/((4/3)*np.pi*((edge[k])**3-(edge[k-1])**3)))*(frequency[i]/P_total)*100 
        mid_pt = (edge[k+1]*edge[k])**(1/2)
        rad_density.append(den)
        mass_pt.append(mid_pt)
    rad_density_comoving = ((1+z)**3)* np.array(rad_density)
    
    #print(rad_density_comoving)
    
    plt.loglog()
    plt.scatter (mass_pt,rad_density_comoving)

halo_min = 100000
halo_max = 101000
file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z0.8/'
b = 10
particle_mass = 2109081520.453063
fraction = 10
z=0.8
SOdensityL1 = 208.4022045135498

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, particle_number,so_radius = halo_info(halo_min,halo_max,file_dir)
X_Y_Z_lists = subsample_data(halo_min, halo_max, file_dir)
rad = radius(x_L2com_X, x_L2com_Y, x_L2com_Z, X_Y_Z_lists)
rad_density_function(rad, particle_mass, b, fraction,z,particle_number)

plt.show()


#print(particle_number)