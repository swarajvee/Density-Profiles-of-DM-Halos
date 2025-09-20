import numpy as np 
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(10,8), dpi = 100)
from mpl_toolkits.mplot3d import Axes3D
ax = plt.axes(projection = '3d')

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

min_val = 0
max_val = 10
size = 200

x, y, z =random_dist(min_val, max_val, size)
x_gauss, y_gauss, z_gauss = gaussian_dist(x, y, z, size)
x_med, y_med, z_med = center(x, y, z)
plotting(x_med, y_med, z_med, x_gauss, y_gauss, z_gauss)

