import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from tqdm import tqdm
fig=plt.figure(figsize=(10,8),dpi=100)
ax = plt.axes(projection='3d')



print("Reading the data")
    
def Halos(file_path):
    data = pd.read_csv(file_path)
    #mass
    N = data['N'].tolist()

    #coordinates
    x = data['X'].tolist()
    y = data['Y'].tolist()
    z = data['Z'].tolist()

    # Create a progress bar
    with tqdm(total=len(x), desc ='Loading Data') as pbar:
        for i in range(len(x)):
            image = ax.scatter(x[i], y[i], z[i], c=N[i], cmap='Greens')
            pbar.update(1)
        plt.colorbar(image, label = 'Mass')
    plt.show()
    print("Done")

file_path = '/Users/swarajv/Education/s10 MSc Major Project/mass function/mass density function per unit volume/Hubble data/csv data/z8.csv'
Halos(file_path)
