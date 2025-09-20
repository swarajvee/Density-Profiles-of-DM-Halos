import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(facecolor='black',figsize=(10,8),dpi=100)
plt.style.use('dark_background')
import os 
import glob


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

    file_paths = glob.glob(os.path.join(file_dir,'halo_info','*halo_info_*.csv'),recursive=True)
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
    file_paths = glob.glob(os.path.join(file_dir,'**','**',f'*{particle_range}*','*halo_info_*.csv'),recursive=True)
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
    return ra

so_central_X,so_central_Y,so_central_Z,x_L2com_X,x_L2com_Y,x_L2com_Z,particle_number,so_radius = halo_info(halo_min,halo_max,file_dir)
x,y,z = subsample_data(halo_min, halo_max, file_dir) 
#rad = radius(x_L2com_X,x_L2com_Y, x_L2com_Z,x,y,z)


plt.scatter(x,y,s=1,label='Subsample Particles')
for i in range(len(particle_number)):
    plt.scatter(so_central_X[i], so_central_Y[i],s=100, label = f'Halo center ({particle_number[i]} particles)')

plt.title(f'Halo Visualization of halos in b/w {halo_min} - {halo_max} particles')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()