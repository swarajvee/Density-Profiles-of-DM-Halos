from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import numpy as np

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

def halo_mass(halos, part_mass):
    halo_mass = []
    for i in range(len(halos)):
        bighalo= cat.halos[i]
        mass = bighalo['N']*part_mass
        halo_mass.append(mass)
    return halo_mass

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

#parameters
part_mass = 2109081520.453063

max_dist, radius = halo_radius(cat.halos['x_L2com'], cat.subsamples['pos'], cat.halos['npoutA'])
mass = halo_mass(cat.halos['x_L2com'], part_mass)

'''print(len(mass))
print(len(cat.halos['x_L2com']))
print(len(radius))'''

