import os
import pandas as pd

#directory
dir_path = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/csv data/z0.1'
count=0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count +=1
#print(count)

data = 0
for i in range(count):
    files= pd.read_csv(os.path.join(dir_path,f'00{str(i)}_z0.1.csv'))
    data +=files

N=data['N'].tolist()
#print(len(N))
