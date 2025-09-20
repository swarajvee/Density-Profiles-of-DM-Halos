from abacusnbody.data.compaso_halo_catalog import CompaSOHaloCatalog
from pathlib import Path
'''import matplotlib.pyplot as plt 
fig = plt.figure(figsize= (10, 8), dpi = 100)''' 
import glob


catdir = '/home/swaraj/Documents/Radial data/z2/halo_info/halo_info_000.asdf'
cat = CompaSOHaloCatalog(catdir, subsamples=dict(A=True), cleaned=False)

mass_A = cat.halos['N'].sum() * cat.header['ParticleSubsampleA']

position = cat.subsamples['pos']

pos = position[0]

x_pos = pos[0:1]
y_pos = pos[1:-1]
z_pos = pos[-2:-1]

print(x_pos, y_pos, z_pos)

#print(pos_strip)