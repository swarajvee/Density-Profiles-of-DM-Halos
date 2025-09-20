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

def plotting(x, y, z, m):
    image = ax.scatter(x,y,z, s= np.array(m)*25, c=m)
    plt.colorbar(image)
    plt.show()

min_val = 0
max_val = 10
size = 20

x, y, z, m =random_dist(min_val, max_val, size)
plotting(x, y, z, m)

