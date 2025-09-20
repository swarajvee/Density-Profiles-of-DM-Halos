import numpy as np 
import matplotlib.pyplot as plt 


def overdensity_boundary(radius,h,k):
    x = np.linspace(h - radius, h + radius, 1000)
    y1 = np.sqrt(radius**2 - (x - h)**2) + k
    y2 = -np.sqrt(radius**2 - (x - h)**2) + k
    return x,y1,y2

radius = 6
h = 1
k = 1

x, y1, y2 = overdensity_boundary(radius,h,k)

plt.plot(x,y1,color='r')
plt.plot(x, y2,color='r')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()