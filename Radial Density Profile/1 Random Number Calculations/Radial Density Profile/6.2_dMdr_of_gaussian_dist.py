import numpy as np 
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(10,8), dpi = 100)
#from mpl_toolkits.mplot3d import Axes3D
#ax = plt.axes(projection = '3d')

def random_dist(min_val,max_val,size):
    x = []
    y=[]
    z=[]
    for j in range(size):
        xi = np.random.randint(min_val, max_val, size= size, dtype=int)
        yi = np.random.randint(min_val, max_val, size= size, dtype=int)
        zi = np.random.randint(min_val, max_val, size= size, dtype=int)
        x.append(xi)
        y.append(yi)
        z.append(zi)
    return x, y, z

def gaussian_dist(x, y, z, size):
    mu_x = np.mean(x)
    mu_y = np.mean(y)
    mu_z = np.mean(z)

    sigma_x =  np.std(x)
    sigma_y =  np.std(y)
    sigma_z =  np.std(z)

    x_gauss = np.random.normal(mu_x, sigma_x, size=size)
    y_gauss = np.random.normal(mu_y, sigma_y, size=size)
    z_gauss = np.random.normal(mu_z, sigma_z, size=size)

    return x_gauss, y_gauss, z_gauss

def center(x, y, z):
    x_med = np.median(x)
    y_med = np.median(y)
    z_med = np.median(z)
    return x_med, y_med, z_med

def plotting(x_med, y_med, z_med,x_gauss, y_gauss, z_gauss):
    image1 = ax.scatter(x_med, y_med, z_med, c= 'red')
    image2 = ax.scatter(x_gauss, y_gauss, z_gauss, c='blue')
    plt.colorbar(image1,label='center particle')
    plt.colorbar(image2, label='small particles')
    plt.show()

def rad_distance(x_med, y_med, z_med, x_gauss, y_gauss, z_gauss):
    distance = []
    for i in range(len(x_gauss)):
        dist = np.sqrt((x_gauss[i]-x_med)**2 + (y_gauss[i]-y_med)**2 + (z_gauss[i]-z_med)**2)
        distance.append(dist)
    return distance

def dMdr(distance,particle_mass, b):
    bineq = np.linspace(min(distance),max(distance),b)
    frequency, bin_edge = np.histogram(distance, bins=bineq)

    bin_mass = []
    for i in range(len(frequency)):
        mass = frequency[i]*particle_mass
        bin_mass.append(mass)
    density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = (bin_mass[k]/((4/3)*np.pi*(bin_edge[k])**3))*(4*np.pi*(bin_edge[k])**2)
        mid_pt = (bin_edge[k+1]+bin_edge[k])/2
        density.append(den)
        mass_pt.append(mid_pt)

    return density, mass_pt

min_val = 0
max_val = 10
size = 200
particle_mass=1
b=10

x, y, z =random_dist(min_val, max_val, size)
x_gauss, y_gauss, z_gauss = gaussian_dist(x, y, z, size)
x_med, y_med, z_med = center(x, y, z)
distance = rad_distance(x_med, y_med, z_med, x_gauss, y_gauss, z_gauss)
#plotting(x_med, y_med, z_med, x_gauss, y_gauss, z_gauss)

density, mass_pt = dMdr(distance,particle_mass, b)
print(mass_pt)

plt.plot(density, mass_pt)
plt.title('Radial Density Function of a Gaussian Distribution')
plt.xlabel('Radius')
plt.ylabel('Radial Density Function')
plt.grid(linestyle='--')
plt.show()