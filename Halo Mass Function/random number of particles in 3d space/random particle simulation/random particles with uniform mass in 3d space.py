import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 
fig=plt.figure(figsize=(10,8),dpi=100)
ax = plt.axes(projection='3d')

def Random_particles(start,end,number_of_particles):
    coordinates = []
    for i in range(number_of_particles):
        x = np.random.uniform(start,end,size=None)
        y = np.random.uniform(start,end,size=None)
        z = np.random.uniform(start,end,size=None)
        coordinates.append((x,y,z))
    x,y,z = zip(*coordinates)    
    ax.scatter(x,y,z)
    plt.show()
    
Random_particles(0,10,1000)

    
