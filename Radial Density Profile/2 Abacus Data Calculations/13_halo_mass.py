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

#parameters
part_mass = 2109081520.453063

mass = halo_mass(cat.halos['x_L2com'], part_mass)
print(len(mass))