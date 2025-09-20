from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8), dpi=100)

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

def halo_mass(halos):
    halo_size = []
    for i in range(len(halos)):
        bighalo= cat.halos[i]
        size = bighalo['N']
        halo_mass.append(size)
    return halo_size

def halo_radius(halos, particles, counts):
    L = cat.header['BoxSize']
    k = 0
    maxdist = np.float32(-1.)
    radius = []
    for i in range(len(halos)):
        cen = halos[i]
        for j in range(counts[i]):
            diff = cen - particles[k + j]
            for m in range(len(diff)):
                if diff[m] > L/2:
                    diff[m] -= L
                if diff[m] < -L/2:
                    diff[m] += L
            dist = np.sqrt((diff**2).sum(-1))
            if dist > maxdist:
                maxdist = dist
        radius.append(dist)
        k += counts[i]
    return maxdist, radius

def rad_density_function(radius, part_mass, b):
    bineq = np.logspace(np.min(np.log10(radius)),np.max(np.log10(radius)),b)
    frequency, bin_edge = np.histogram(radius, bins=bineq)

    bin_mass = []
    for i in range(len(frequency)):
        mass = frequency[i]*part_mass
        bin_mass.append(mass)
    density = []  
    mass_pt = []  
    for k in range(len(bin_edge)-1):
        den = bin_mass[k]/((4/3)*np.pi*(bin_edge[k])**3)
        mid_pt = (bin_edge[k+1]*bin_edge[k])**2 #geometric mean
        density.append(den)
        mass_pt.append(mid_pt)

    return density, mass_pt

#parameters
part_mass = 2109081520.453063
b=10

max_dist, radius = halo_radius(cat.halos['x_L2com'], cat.subsamples['pos'], cat.halos['npoutA'])
#halo_size = halo_mass(cat.halos['x_L2com'])
density, mass_pt = rad_density_function(radius, part_mass, b)

plt.loglog()
plt.scatter(mass_pt, density)
plt.show()
