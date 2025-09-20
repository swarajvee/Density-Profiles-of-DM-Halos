import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,8),dpi=100)
import os 
import glob

particle_range = '100000-101000'
file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z0.8/'
file_paths = glob.glob(os.path.join(file_dir,'**','**',f'*{particle_range}*','*halo_info_*.csv'),recursive=True)

def subsample_data(file_paths):
    X=[]
    Y=[]
    Z=[]
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

x,y,z = subsample_data(file_paths)
