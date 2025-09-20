import pandas as pd 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi = 100)

def cosmos(filepath):
    data= pd.read_csv(filepath)
    x = data['x'].tolist()
    y = data['y'].tolist()
    z = data['z'].tolist()
    #plt.style.use('dark_background')
    plt.scatter(y, z, s =0.7, c = x,cmap='magma')
    plt.colorbar()
    plt.grid()
    plt.show()
filepath = '/Volumes/Swaraj\'s\ Backup/Projects/Density\ Profiles\ of\ Dark\ Matter\ Halos\ \(git\)/HubbleData/Radial\ Density\ Profile/high\ base/z0.8/subsample\ data/halo_info_000_subsample_data.csv'
cosmos(filepath)
