import numpy as np 
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(10,8),dpi=100)
ax = plt.axes(projection='3d')

def Random_particles(l,n):
    coordinates = []
    mu=100
    sigma=50
    for i in range(n):
        x = random.gauss(mu,sigma)
        y = random.gauss(mu,sigma)
        z = random.gauss(mu,sigma)
        m = random.gauss(mu,sigma)
        coordinates.append((x,y,z,m))
    x,y,z,m = zip(*coordinates)
    image = ax.scatter(x,y,z, s=np.array(m), c=m)
    plt.colorbar(image, label = 'Mass')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()

l = 10 # side length
v = l**3 # volume
n = 1000 # number of particles

Random_particles(l,n)
