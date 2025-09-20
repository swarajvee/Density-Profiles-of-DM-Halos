#import numba
from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
import numpy as np

file = 'halo_info_000'
cat = CompaSOHaloCatalog('/home/swaraj/Documents/Radial data/z2/halo_info/'+file+'.asdf', cleaned=False,subsamples=dict(A=True, B=True))

L = cat.header['BoxSize']

def find_farthest(halos, particles, counts):
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

max_dist, radius = find_farthest(cat.halos['x_L2com'], cat.subsamples['pos'], cat.halos['npoutA'])
#print(max_dist)