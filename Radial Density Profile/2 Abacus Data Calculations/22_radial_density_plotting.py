import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,8), dpi=100)

file_dir = '/Users/swarajv/Education/s10 MSc Major Project/Hubble data/Radial Density Profile/high base/z2'
file_name = 'halo_info_000'

def halo_info(file_dir,file_name):
    halo = pd.read_csv(file_dir+'/halo_info/'+file_name+'.csv')
    so_central_X = halo['SO_central_particle_X']
    so_central_Y = halo['SO_central_particle_Y']
    so_central_Z = halo['SO_central_particle_Z']

    x_L2com_X = halo['x_L2com_X']
    x_L2com_Y = halo['x_L2com_Y']
    x_L2com_Z = halo['x_L2com_Z']
    
    particle_number =halo['N']
    max_index = np.argmax(particle_number)
    #print(np.max(halo['N']))
    return so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, max_index

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
    rad = np.sqrt((x_sub-x_cent)**2+(y_sub-y_cent)**2+(z_sub-z_cent)**2)
    return rad

def rad_density_function(radius, particle_mass, b, fraction):

    bineq = np.logspace(np.min(np.log10(radius)),np.max(np.log10(radius)),b)
    frequency, bin_edge = np.histogram(radius, bins=bineq)

    bin_mass = []
    for i in range(len(frequency)):
        mass = frequency[i]*particle_mass
        bin_mass.append(mass)
    rad_density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = ((bin_mass[k])/((4/3)*np.pi*((bin_edge[k])**3-(bin_edge[k-1])**3)))*fraction
        mid_pt = (bin_edge[k+1]*bin_edge[k])**(1/2)
        rad_density.append(den)
        mass_pt.append(mid_pt)

    return rad_density, mass_pt


b = 10
particle_mass = 2109081520.453063
fraction = 10


so_central_X, so_central_Y, so_central_Z, x_L2com_X, x_L2com_Y, x_L2com_Z, max_index = halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(so_central_X[max_index],so_central_Y[max_index], so_central_Z[max_index],X,Y,Z)
rad_density, mass_pt = rad_density_function(rad, particle_mass, b, fraction)


plt.loglog()
plt.scatter(mass_pt, rad_density)
plt.grid()
plt.show()