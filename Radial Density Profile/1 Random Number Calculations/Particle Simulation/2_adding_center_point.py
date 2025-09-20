import numpy as np 
import matplotlib.pyplot as plt
fig= plt.figure(figsize=(10,8), dpi = 100)
from mpl_toolkits.mplot3d import Axes3D
ax = plt.axes(projection = '3d')

def random_dist(min_val,max_val,size):
    x = []
    y=[]
    z=[]
    m =[]
    for j in range(size):
        xi = np.random.randint(min_val, max_val, size= size, dtype=int)
        yi = np.random.randint(min_val, max_val, size= size, dtype=int)
        zi = np.random.randint(min_val, max_val, size= size, dtype=int)
        mi = np.random.randint(min_val, max_val, size= size, dtype=int)
        x.append(xi)
        y.append(yi)
        z.append(zi)
        m.append(mi)
    return x, y, z, m
def center(x, y, z, m):
    x_med = np.median(x)
    y_med = np.median(y)
    z_med = np.median(z)
    m_med = np.median(m)
    return x_med, y_med, z_med, m_med

def plotting(x_med, y_med, z_med, m_med, x, y, z, m):
    image1 = ax.scatter(x_med, y_med, z_med, s= m_med*900, c=m_med)
    image2 = ax.scatter(x,y,z, s= np.array(m)*25, c=m)
    plt.colorbar(image1,label='center particle')
    plt.colorbar(image2, label='small particles')
    plt.show()

min_val = 0
max_val = 10
size = 20

x, y, z, m =random_dist(min_val, max_val, size)
x_med, y_med, z_med, m_med = center(x, y, z, m)
plotting(x_med, y_med, z_med, m_med, x, y, z, m)

