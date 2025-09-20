import pandas as pd 
import numpy as np 

file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2'
file_name = 'halo_info_000'

def halo_info(file_dir,file_name):
    halo = pd.read_csv(file_dir+'/halo_info/'+file_name+'.csv')
    so_central_X = halo['SO_central_particle_X']
    so_central_Y = halo['SO_central_particle_Y']
    so_central_Z = halo['SO_central_particle_Z']
    
    particle_number =halo['N']
    max_index = np.argmax(particle_number)
    return so_central_X, so_central_Y, so_central_Z, max_index

def subsample(file_dir, file_name):
    subsamples = pd.read_csv(file_dir+'/subsample data/'+file_name+'_subsample_data.csv')

    Subsample_A_X = subsamples['Subsample_A_X']
    Subsample_A_Y = subsamples['Subsample_A_Y']
    Subsample_A_Z = subsamples['Subsample_A_Z']

    Subsample_B_X = subsamples['Subsample_B_X']
    Subsample_B_Y = subsamples['Subsample_B_Y']
    Subsample_B_Z = subsamples['Subsample_B_Z']
    
    Subsample_X = np.vstack((Subsample_A_X,Subsample_B_X))
    X_clean = Subsample_X[~np.isnan(Subsample_X)]

    Subsample_Y = np.vstack((Subsample_A_Y,Subsample_B_Y))
    Y_clean = Subsample_Y[~np.isnan(Subsample_Y)]

    Subsample_Z = np.vstack((Subsample_A_Z,Subsample_B_Z))
    Z_clean = Subsample_Z[~np.isnan(Subsample_Z)]
    return X_clean, Y_clean, Z_clean

def radius(x_cent,y_cent,z_cent, x_sub,y_sub,z_sub):
    rad = np.sqrt((x_sub-x_cent)**2+(y_sub+y_cent)**2+(z_sub-z_cent)**2)
    return rad

so_central_X, so_central_Y, so_central_Z, max_index= halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(so_central_X[max_index],so_central_Y[max_index], so_central_Z[max_index],X,Y,Z)

#print(so_central_X[max_index],so_central_Y[max_index], so_central_Z[max_index])

