import numpy as np 
import matplotlib.pyplot as plt 
fig= plt.figure(figsize=(10,8),dpi=100)
from hmf import MassFunction

mf= MassFunction()
for z in np.linspace(0,8,100):
    mf.update(z=z)
    plt.loglog()
    plt.plot(mf.m, mf.dndm, alpha=1-(z/10), lw =0.9)

plt.grid()
plt.show()

