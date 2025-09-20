import pandas as pd 
import numpy as np 

file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2'
file_name = 'halo_info_000'



def halo_info(file_dir,file_name):
    halo = pd.read_csv(file_dir+'/halo_info/'+file_name+'.csv')
    print(halo)

def subsample(file_dir, file_name):
    subsamples = pd.read_csv(file_dir+'/subsample data/'+file_name+'_subsample_data.csv')
    print(subsamples)

halo_info(file_dir, file_name)
subsample(file_dir, file_name)