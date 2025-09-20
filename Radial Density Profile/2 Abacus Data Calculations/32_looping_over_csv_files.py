import numpy as np 
import pandas as pd 
import glob
import os
import re

file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z0.8'
file_paths = glob.glob(os.path.join(file_dir,'**','**','**', f'halo_info_003_subsample_data_''*.csv'),recursive=True)

no_of_particles = []
halo_file_names = []
for file_path in file_paths:
    file_name = file_path.split('/')[-1]
    part_strip=['halo_info_003_subsample_data_','.csv']
    particles = file_name.strip(str(part_strip))

    halo_strip=['halo_info_','_subsample_data_',particles,'.csv']
    halo_file = file_name.strip(str(halo_strip))

    no_of_particles.append(particles)
    halo_file_names.append(halo_file)

#print(no_of_particles)
print(halo_file_names)