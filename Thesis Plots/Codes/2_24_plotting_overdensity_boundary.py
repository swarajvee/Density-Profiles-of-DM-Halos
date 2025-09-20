import pandas as pd 
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('dark_background')
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

    so_radius = halo['SO_radius']
    r100_L2com = halo['r100_L2com']
    return so_central_X, so_central_Y, so_central_Z,x_L2com_X, x_L2com_Y, x_L2com_Z, max_index, so_radius, r100_L2com, particle_number

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

def overdensity_boundary(radius,h,k):
    x = np.linspace(h - radius, h + radius, 1000)
    y1 = np.sqrt(radius**2 - (x - h)**2) + k
    y2 = -np.sqrt(radius**2 - (x - h)**2) + k
    return x,y1,y2

b = 10
particle_mass = 2109081520.453063
fraction = 10

so_central_X, so_central_Y, so_central_Z,x_L2com_X, x_L2com_Y, x_L2com_Z, max_index, so_radius, r100_L2com, particle_number = halo_info(file_dir, file_name)
X, Y, Z = subsample(file_dir, file_name)
rad = radius(x_L2com_X[max_index],x_L2com_Y[max_index], x_L2com_Z[max_index],X,Y,Z)
x,y1,y2 = overdensity_boundary(so_radius[max_index],so_central_X[max_index],so_central_Y[max_index])

#print(np.max(rad))
plt.scatter(so_central_X[max_index], so_central_Y[max_index], s = 100, label=f'Halo Center: {np.round(so_central_X[max_index],3), np.round(so_central_Y[max_index],3)}', color='white')
plt.scatter(X, Y, s=1, label ='Subsamples', alpha=0.5)
plt.plot(x,y1,color='r', label=f'SO radius: {np.round(so_radius[max_index],3)} [Mpc $h^{-1}$]')
plt.plot(x,y2,color='r')

#plt.Circle((so_central_X[max_index], so_central_Y[max_index]), np.max(rad), label='SO',color='r', fill=False)

plt.title(f'Halo with {particle_number[max_index]} particles')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()