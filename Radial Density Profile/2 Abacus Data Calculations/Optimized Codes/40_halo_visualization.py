import glob
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(15,8),dpi=100,facecolor='black')
plt.style.use('dark_background')

halo_min = 100000
halo_max = 101000
z=0.8
b = 10
particle_mass = 2109081520.453063
SOdensityL1 = 208.4022045135498
file_dir = f'/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z{z}/'

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

so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, particle_number,so_radius, r100 = halo_info(halo_min,halo_max,file_dir)
X_Y_Z_lists = subsample_data(halo_min, halo_max, file_dir)

for i in range(len(particle_number)):
    plt.scatter(X_Y_Z_lists[i][1],X_Y_Z_lists[i][2],label=f'{particle_number[i]}')
    #plt.scatter(x_L2com_Y[i], x_L2com_Z[i], color='red')
plt.title(f'Halos with subsamples b/w {halo_min}-{halo_max}')
plt.xlabel('y')
plt.ylabel('z')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1),title='No of Subsamples')
plt.show()