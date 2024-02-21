import os
import glob
import pandas as pd

dir_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z0.1'
files = glob.glob(os.path.join(dir_path,'*z*.csv'))

#print(files)

data_final= []
for i in range(len(files)):
    data= pd.read_csv(f'{files[i]}')
    data_final.append(data)

all_data= pd.concat(data_final)
N = all_data['N'].tolist()
print(N[18301383])


