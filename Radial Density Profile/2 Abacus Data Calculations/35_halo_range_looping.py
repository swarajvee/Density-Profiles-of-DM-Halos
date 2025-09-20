import pandas as pd 
import numpy as np
import os 
import glob

particle_range = '100000-101000'
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

so_central_X,so_central_Y,so_central_Z,x_L2com_X,x_L2com_Y,x_L2com_Z,particle_number,so_radius = halo_info(halo_min,halo_max,file_dir)